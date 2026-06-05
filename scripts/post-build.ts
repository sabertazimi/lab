#!/usr/bin/env node

/**
 * Post-build script for lab monorepo
 *
 * This script handles moving build outputs from individual packages
 * to the root dist/ directory with proper path normalization.
 *
 * Usage:
 *   node scripts/post-build.ts [package-name]
 *
 * If no package name is provided, it will process all packages.
 */

import fs from 'node:fs'
import path from 'node:path'
import process from 'node:process'
import { fileURLToPath } from 'node:url'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
const RootDir = path.resolve(__dirname, '..')
const PackagesDir = path.join(RootDir, 'packages')
const DistDir = path.join(RootDir, 'dist')

/** Package configuration for post-build processing */
interface PackageConfig {
  /** Package name */
  name: string
  /** Build type */
  type: 'react-router' | 'vite'
  /** Build output directory relative to package */
  buildDir: string
  /** Destination directory name (defaults to package name) */
  destDir?: string
  /** Whether this is the root index.html package */
  isRoot?: boolean
  /** Subdirectory containing index.html for React Router projects */
  normalizeSubDir?: string
  /** Additional files/folders to copy */
  extraCopy?: string[]
}

/** Get package configurations */
function getPackageConfigs(): PackageConfig[] {
  return [
    {
      name: 'portfolio',
      type: 'react-router',
      buildDir: 'build/client',
      isRoot: true,
    },
    {
      name: 'm-league-reviewer',
      type: 'react-router',
      buildDir: 'build/client',
      normalizeSubDir: 'm-league-reviewer',
    },
    {
      name: 'dblp',
      type: 'vite',
      buildDir: 'dist',
    },
    {
      name: 'react-renderer',
      type: 'vite',
      buildDir: 'dist',
    },
    {
      name: 'mortal-ui',
      type: 'vite',
      buildDir: 'dist',
      extraCopy: ['e2e'],
    },
    {
      name: 'echarts-dashboard',
      type: 'vite',
      buildDir: 'dist',
    },
    {
      name: 'vue-trello',
      type: 'vite',
      buildDir: 'dist',
    },
    {
      name: 'vue-design',
      type: 'vite',
      buildDir: 'dist',
    },
  ]
}

/**
 * Recursively copy directory with optional exclusion
 * @param src - Source directory
 * @param dest - Destination directory
 * @param excludePaths - Set of absolute paths to exclude
 */
function copyDirSync(
  src: string,
  dest: string,
  excludePaths: Set<string> = new Set(),
): void {
  if (!fs.existsSync(src)) {
    console.warn(`  ⚠️  Source does not exist: ${src}`)
    return
  }

  fs.mkdirSync(dest, { recursive: true })

  const entries = fs.readdirSync(src, { withFileTypes: true })

  for (const entry of entries) {
    const srcPath = path.join(src, entry.name)
    const destPath = path.join(dest, entry.name)

    // Skip excluded paths
    if (excludePaths.has(srcPath)) {
      continue
    }

    if (entry.isDirectory()) {
      copyDirSync(srcPath, destPath, excludePaths)
    } else {
      fs.copyFileSync(srcPath, destPath)
    }
  }
}

/**
 * Get the first segment of a path (top-level directory name)
 * @param relativePath - Relative path like 'lab' or 'lab/m-league-reviewer'
 * @returns First segment of the path
 */
function getFirstPathSegment(relativePath: string): string {
  return relativePath.split('/')[0]
}

/**
 * Find the directory containing index.html in React Router build output
 * @param clientDir - The client build directory
 * @returns Path to directory containing index.html, or null if not found
 */
function findIndexHtmlDir(clientDir: string): string | null {
  if (!fs.existsSync(clientDir)) {
    return null
  }

  // Check if index.html exists directly in clientDir
  if (fs.existsSync(path.join(clientDir, 'index.html'))) {
    return clientDir
  }

  // Search recursively for index.html
  const searchDir = (dir: string): string | null => {
    const entries = fs.readdirSync(dir, { withFileTypes: true })

    for (const entry of entries) {
      if (entry.isDirectory()) {
        const subDir = path.join(dir, entry.name)
        if (fs.existsSync(path.join(subDir, 'index.html'))) {
          return subDir
        }
        const found = searchDir(subDir)
        if (found)
          return found
      }
    }
    return null
  }

  return searchDir(clientDir)
}

/**
 * Process a single package
 * @param config - Package configuration
 */
function processPackage(config: PackageConfig): void {
  const packageDir = path.join(PackagesDir, config.name)
  const buildDir = path.join(packageDir, config.buildDir)
  const destDir = config.isRoot
    ? DistDir
    : path.join(DistDir, config.destDir || config.name)

  console.log(`\n📦 Processing: ${config.name}`)

  // Check if build directory exists
  if (!fs.existsSync(buildDir)) {
    console.log(
      `  ⏭️  Skipping - build directory not found: ${config.buildDir}`,
    )
    return
  }

  // Create destination directory
  fs.mkdirSync(destDir, { recursive: true })

  if (config.type === 'react-router') {
    // Handle React Router v7 projects with nested build structure
    const normalizedDir = config.normalizeSubDir
      ? path.join(buildDir, config.normalizeSubDir)
      : findIndexHtmlDir(buildDir)

    if (config.isRoot) {
      // For root package (portfolio), copy index.html to dist root
      if (
        normalizedDir
        && fs.existsSync(path.join(normalizedDir, 'index.html'))
      ) {
        fs.copyFileSync(
          path.join(normalizedDir, 'index.html'),
          path.join(DistDir, 'index.html'),
        )
        console.log(`  ✅ Copied index.html to dist/`)

        // Copy remaining client files to dist root, excluding the normalizeSubDir
        const excludePaths = config.normalizeSubDir
          ? new Set([path.join(buildDir, getFirstPathSegment(config.normalizeSubDir))])
          : new Set()
        copyDirSync(buildDir, DistDir, excludePaths)
        console.log(`  ✅ Copied remaining client files to dist/`)
      } else {
        // Fallback: just copy everything
        copyDirSync(buildDir, DistDir)
        console.log(`  ✅ Copied all files to dist/`)
      }
    } else {
      // For sub-packages like m-league-reviewer
      if (normalizedDir && fs.existsSync(normalizedDir)) {
        // Copy the normalized directory to destination
        copyDirSync(normalizedDir, destDir)
        console.log(`  ✅ Copied ${config.normalizeSubDir} to ${config.name}/`)

        // Copy remaining client files (assets, etc.), excluding the normalizeSubDir parent
        const excludePaths = new Set([
          path.join(buildDir, getFirstPathSegment(config.normalizeSubDir!)),
        ])
        copyDirSync(buildDir, destDir, excludePaths)
        console.log(`  ✅ Copied remaining client files`)
      } else {
        // Fallback: copy everything
        copyDirSync(buildDir, destDir)
        console.log(`  ✅ Copied all files to ${config.name}/`)
      }
    }
  } else {
    // Handle Vite projects (simple copy)
    copyDirSync(buildDir, destDir)
    console.log(
      `  ✅ Copied ${config.buildDir}/ to ${config.destDir || config.name}/`,
    )
  }

  // Handle extra copy items
  if (config.extraCopy) {
    for (const item of config.extraCopy) {
      const srcPath = path.join(packageDir, item)
      const destPath = path.join(destDir, item)

      if (fs.existsSync(srcPath)) {
        if (fs.statSync(srcPath).isDirectory()) {
          copyDirSync(srcPath, destPath)
        } else {
          fs.copyFileSync(srcPath, destPath)
        }
        console.log(`  ✅ Copied extra: ${item}`)
      } else {
        console.warn(`  ⚠️  Extra item not found: ${item}`)
      }
    }
  }
}

/** Main entry point */
function main(): void {
  const args = process.argv.slice(2)
  const targetPackage = args[0]
  const packageConfigs = getPackageConfigs()

  console.log('🚀 Post-build script for lab monorepo')
  console.log(`   Root: ${RootDir}`)
  console.log(`   Dist: ${DistDir}`)

  // Ensure clean dist directory
  fs.rmSync(DistDir, { recursive: true, force: true })
  fs.mkdirSync(DistDir, { recursive: true })

  if (targetPackage) {
    // Process single package
    const config = packageConfigs.find(c => c.name === targetPackage)
    if (!config) {
      console.error(`\n❌ Unknown package: ${targetPackage}`)
      console.log(
        `   Available packages: ${packageConfigs.map(c => c.name).join(', ')}`,
      )
      process.exit(1)
    }
    processPackage(config)
  } else {
    // Process all packages
    for (const config of packageConfigs) {
      processPackage(config)
    }
  }

  console.log('\n✨ Post-build complete!')
}

main()
