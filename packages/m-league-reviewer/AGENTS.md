# AGENTS.md

This file provides guidance to coding agents when working with code in this repository.

## Project Overview

M.League Reviewer is a React-based web application for reviewing and analyzing M.League (Japanese professional mahjong league) daily matches. The application displays match data in a table format, allowing users to record and analyze professional players' tile selection decisions.

## Common Commands

```bash
# Install dependencies (always run first)
pnpm install

# Start development server
pnpm run dev

# Build for production
pnpm run build

# Lint code and run type checking
pnpm run lint

# Run tests with coverage
pnpm run test

# Type check only
pnpm run lint:typecheck

# Fetch game data from external sources
pnpm run fetch

# Fetch game schedule only
pnpm run fetch:game-schedule
```

## Architecture Overview

### Technology Stack

- **React Router (Framework Mode)** - Routing with SSR support
- **TypeScript** - Type safety throughout the application
- **Vite** - Build tool and dev server
- **Tailwind CSS** - Styling framework
- **Shadcn UI** - Pre-built UI components (Radix UI based)
- **Zustand** - State management with persistence
- **TipTap** - Rich text editor for notes

### Key Architectural Patterns

1. **Route-based Organization**: Uses React Router's file-based routing with `routes.ts` configuration
2. **Component Architecture**:
   - UI components in `src/components/ui/` (Shadcn, do not modify directly)
   - Custom components in `src/components/`
   - View components in `src/views/`
   - Route components in `src/routes/`

3. **State Management**:
   - Zustand stores in `src/stores/` with localStorage persistence
   - Two main stores: `reviews.ts` and `notes.ts`
   - Type-safe state with proper validation

4. **Data Flow**:
   - API layer in `src/api/` handles data fetching and transformation
   - Data fetching scripts in `scripts/` (run directly with Node.js v24+ native TS support)
   - External data sources include M.League official site and QQQ sheets

### Project Structure

```plaintext
src/
├── api/          # Data fetching and external API integration
├── components/   # React components
│   └── ui/       # Shadcn UI components (do not modify)
├── routes/       # Route components for file-based routing
├── views/        # Page-level view components
├── hooks/        # Custom React hooks
├── lib/          # Utility functions
├── stores/       # Zustand state management
└── assets/       # Static assets and global styles
```

### Important Implementation Details

1. **Build Process**: Uses custom post-build script to move files to `../../dist/m-league-reviewer`
2. **Path Aliases**: `@/*` mapped to `src/*` in tsconfig
3. **Data Persistence**: Reviews and notes persist in localStorage via Zustand
4. **Type Safety**: Strict TypeScript mode with comprehensive type definitions
5. **Testing**: Vitest with coverage reporting
6. **Linting**: ESLint with custom config, includes type checking

### Development Notes

- Package manager: **pnpm only** (never npm/yarn)
- Development server runs on default Vite port (5173)
- React Router uses Framework Mode with SSR
- All UI components use Tailwind CSS with Shadcn theming
- Icon library: Lucide React
- Date handling: date-fns library

### Data Model

- **Reviews**: Match reviews with teams, tables, status tracking
- **Notes**: Rich text notes with TipTap editor integration
- **Players**: Player information and selection components
- **Calendar**: Game schedule and date navigation

### Build Outputs

- Client build: `./build/client/`
- Server build: `./build/server/`
- Final output: `../../dist/m-league-reviewer/` (after post-build script)

## Constraints

- DO NOT add Claude co-authorship footer to commits
