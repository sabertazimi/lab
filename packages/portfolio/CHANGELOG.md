# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

### Features

- **bash-agent:** initialize minimal Claude Code learning project ([#938](https://github.com/sabertazimi/lab/issues/938)) ([3e7dd4f](https://github.com/sabertazimi/lab/commit/3e7dd4f86fb00176ca69294d39af751e3b29286a))

### Performance Improvements

- [ImgBot] optimize images ([#937](https://github.com/sabertazimi/lab/issues/937)) ([4f59b84](https://github.com/sabertazimi/lab/commit/4f59b842c4496c14bd45c56670c7190ec0538f10))

# [3.0.0](https://github.com/sabertazimi/lab/compare/v2.5.0...v3.0.0) (2026-01-28)

- feat(rust)!: add rust learning workspace with rustlings, exercism, and docs (#935) ([cfa6854](https://github.com/sabertazimi/lab/commit/cfa6854932c3bf4476e99c39403c621320f89916)), closes [#935](https://github.com/sabertazimi/lab/issues/935)

### Features

- **dblp:** add DBLP search application ([#936](https://github.com/sabertazimi/lab/issues/936)) ([1faf657](https://github.com/sabertazimi/lab/commit/1faf657f95c5ed766ee0d82caa7baa1b1ef0845f))
- **portfolio:** add Rust notes to portfolio ([dc7b574](https://github.com/sabertazimi/lab/commit/dc7b57485799234a7a3acb80118de87d7841a5f7))

### BREAKING CHANGES

- add Rust workspace to monorepo root, modifies CI workflow and project structure

* Add root Cargo workspace configuration with rustfmt and mdbook setup
* Add basis crate with git, list/stack, and time utility modules
* Add exercism hello-world exercise
* Add rustlings exercises covering variables, functions, enums, structs, collections, strings, modules, macros, move_semantics, generics, option, error_handling, traits, tests, threads, standard_library_types, conversions, advanced_errors
* Add comprehensive rust documentation notes
* Update CI workflow with rust checks
* Update gitignore for rust build artifacts

- ci(vercel): add build script

- ci(vercel): setup mdbook

- refactor: remove vercel deployment and simplify base path config

* Remove vercel.json and all VERCEL environment detection
* Simplify base path to '/' for portfolio (root) and '/{package}/' for sub-packages
* Add CNAME for GitHub Pages custom domain
* Clean up post-build.js by removing vercel-specific normalizeSubDir logic

Co-authored-by: Cursor <cursoragent@cursor.com>

# [2.5.0](https://github.com/sabertazimi/lab/compare/v2.4.0...v2.5.0) (2025-12-23)

### Features

- **build:** add Vercel deployment support with centralized post-buil… ([#921](https://github.com/sabertazimi/lab/issues/921)) ([1a2bbe5](https://github.com/sabertazimi/lab/commit/1a2bbe5dfbe0c36d18ad2c2d24343a332fe5e61f))

### Performance Improvements

- [ImgBot] optimize images ([#923](https://github.com/sabertazimi/lab/issues/923)) ([b5a6a56](https://github.com/sabertazimi/lab/commit/b5a6a56d9543b897a669f8a4f9a23cf2af5bdfd8))

# [2.4.0](https://github.com/sabertazimi/lab/compare/v2.3.0...v2.4.0) (2025-12-21)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#914](https://github.com/sabertazimi/lab/issues/914)) ([5cf2bd4](https://github.com/sabertazimi/lab/commit/5cf2bd48ed243f1e590a320bd8af730bebe629ed))

# [2.3.0](https://github.com/sabertazimi/lab/compare/v2.2.0...v2.3.0) (2025-12-15)

**Note:** Version bump only for package @lab/lab

# [2.2.0](https://github.com/sabertazimi/lab/compare/v2.1.0...v2.2.0) (2025-12-12)

**Note:** Version bump only for package @lab/lab

# [2.1.0](https://github.com/sabertazimi/lab/compare/v2.0.0...v2.1.0) (2025-12-10)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#870](https://github.com/sabertazimi/lab/issues/870)) ([f3d83b1](https://github.com/sabertazimi/lab/commit/f3d83b1804abe28ce0053a20df8111ccdd9be45b))

### Performance Improvements

- [ImgBot] optimize images ([#868](https://github.com/sabertazimi/lab/issues/868)) ([c5cd126](https://github.com/sabertazimi/lab/commit/c5cd126855ed1760ba0af55d0d66a3eb493e64a2))

# [2.0.0](https://github.com/sabertazimi/lab/compare/v1.10.0...v2.0.0) (2025-12-04)

### Bug Fixes

- **portfolio:** adjust padding for projects grid ([25b4007](https://github.com/sabertazimi/lab/commit/25b40076a75f3c3a9aba014f2466effe3fe69523))

- feat!(web): add portfolio index page (#866) ([d837d8b](https://github.com/sabertazimi/lab/commit/d837d8b356938ac8157b67e48a7a3326c8278522)), closes [#866](https://github.com/sabertazimi/lab/issues/866)

### Features

- **portfolio:** implement projects portfolio grid ([#867](https://github.com/sabertazimi/lab/issues/867)) ([434ce64](https://github.com/sabertazimi/lab/commit/434ce6410529fda51909803fcd5bb090118b3d75))

### BREAKING CHANGES

- - style: format code
