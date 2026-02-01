# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.2.0](https://github.com/sabertazimi/lab/compare/v3.1.0...v3.2.0) (2026-02-01)

**Note:** Version bump only for package @lab/m-league-reviewer

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

**Note:** Version bump only for package @lab/m-league-reviewer

# [3.0.0](https://github.com/sabertazimi/lab/compare/v2.5.0...v3.0.0) (2026-01-28)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#929](https://github.com/sabertazimi/lab/issues/929)) ([645c3dc](https://github.com/sabertazimi/lab/commit/645c3dcbfd7315294fdde7778c47f4b6aae545ba))
- **deps:** update dependencies (non-major) ([#933](https://github.com/sabertazimi/lab/issues/933)) ([465b4e4](https://github.com/sabertazimi/lab/commit/465b4e407553663fc9d8359950fef8f56459e18e))

- feat(rust)!: add rust learning workspace with rustlings, exercism, and docs (#935) ([cfa6854](https://github.com/sabertazimi/lab/commit/cfa6854932c3bf4476e99c39403c621320f89916)), closes [#935](https://github.com/sabertazimi/lab/issues/935)

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

### Bug Fixes

- **m.league-editor:** add rounded corners to note editor toolbar ([#920](https://github.com/sabertazimi/lab/issues/920)) ([9b94891](https://github.com/sabertazimi/lab/commit/9b94891a119f8ab726d08e1498640b0cd51fbb17))

### Features

- **build:** add Vercel deployment support with centralized post-buil… ([#921](https://github.com/sabertazimi/lab/issues/921)) ([1a2bbe5](https://github.com/sabertazimi/lab/commit/1a2bbe5dfbe0c36d18ad2c2d24343a332fe5e61f))
- **m.league-ui:** add consistent border radius styling across UI components ([#919](https://github.com/sabertazimi/lab/issues/919)) ([b700bc8](https://github.com/sabertazimi/lab/commit/b700bc8fd7d3468ad80f1a3fdc039218adc7354c))

# [2.4.0](https://github.com/sabertazimi/lab/compare/v2.3.0...v2.4.0) (2025-12-21)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#914](https://github.com/sabertazimi/lab/issues/914)) ([5cf2bd4](https://github.com/sabertazimi/lab/commit/5cf2bd48ed243f1e590a320bd8af730bebe629ed))
- **m.league-review:** fix hydration mismatch in calendar view by delaying isToday check ([#913](https://github.com/sabertazimi/lab/issues/913)) ([01efb38](https://github.com/sabertazimi/lab/commit/01efb3845435036380fb9fb6fe453897105fd46c))
- **m.league-review:** remove hover styles and standardize keyboard shortcuts ([#911](https://github.com/sabertazimi/lab/issues/911)) ([fc29c32](https://github.com/sabertazimi/lab/commit/fc29c32af8108bc1eab417be5384bb5210ea5660))
- **m.league-review:** standardize keyboard shortcuts and focus management ([#912](https://github.com/sabertazimi/lab/issues/912)) ([c274dcc](https://github.com/sabertazimi/lab/commit/c274dccc4ae071d3642aeae664095455cf61bd41))

### Features

- **m-league-motion:** add motion animations to major views ([#918](https://github.com/sabertazimi/lab/issues/918)) ([fee6080](https://github.com/sabertazimi/lab/commit/fee608096d02d63ad9780956e0953cc48192b95d))

# [2.3.0](https://github.com/sabertazimi/lab/compare/v2.2.0...v2.3.0) (2025-12-15)

### Bug Fixes

- **m.league-hosetsu:** change shortcuts text to tooltips ([#900](https://github.com/sabertazimi/lab/issues/900)) ([a0888ed](https://github.com/sabertazimi/lab/commit/a0888ed10c7d331ce9de55f1e90b42fa86c8eb82))
- **m.league-layout:** adjust alignment for dialog and section header ([#896](https://github.com/sabertazimi/lab/issues/896)) ([ac4f45e](https://github.com/sabertazimi/lab/commit/ac4f45ea9ebd46e8179de4144a846d3258b6e223))
- **m.league-layout:** adjust site header layout ([#897](https://github.com/sabertazimi/lab/issues/897)) ([758d175](https://github.com/sabertazimi/lab/commit/758d175680cda0a04b18f6a9da245eee1fb30f5e))

### Features

- **m.league-review:** add drag selection from input edges ([#910](https://github.com/sabertazimi/lab/issues/910)) ([c78c7cc](https://github.com/sabertazimi/lab/commit/c78c7ccdd1a655552734b94267f8699f8ed16dbb))
- **m.league-review:** add multi-select and batch operations to table ([#909](https://github.com/sabertazimi/lab/issues/909)) ([acd73f3](https://github.com/sabertazimi/lab/commit/acd73f3264beeb3b8d96d887a86f8235c411fecb))
- **m.league-state:** refactor state management with zustand ([#899](https://github.com/sabertazimi/lab/issues/899)) ([3229cff](https://github.com/sabertazimi/lab/commit/3229cff891cdceec3cf5d53db6e5d4a8d15a0d37))

# [2.2.0](https://github.com/sabertazimi/lab/compare/v2.1.0...v2.2.0) (2025-12-12)

### Bug Fixes

- **m.league-editor:** add tooltip to toolbar ([#883](https://github.com/sabertazimi/lab/issues/883)) ([3471063](https://github.com/sabertazimi/lab/commit/34710631c03d804bce24702d51a2cb7953a3d383))
- **m.league-editor:** adjust width and height layouts ([#885](https://github.com/sabertazimi/lab/issues/885)) ([fe3ef8d](https://github.com/sabertazimi/lab/commit/fe3ef8d6944f2c9a80fcd472791dd875a17757bd))
- **m.league-editor:** remove border radius of editor toolbar ([#884](https://github.com/sabertazimi/lab/issues/884)) ([1e2c701](https://github.com/sabertazimi/lab/commit/1e2c70171fba11ee56f9fb43ab0d535195bda54d))
- **m.league-hosetsu:** implement hosetsu type input cut feature ([#894](https://github.com/sabertazimi/lab/issues/894)) ([c15c0e6](https://github.com/sabertazimi/lab/commit/c15c0e6e108250aa0f5d11fce7d76ab2d522f8d9))
- **m.league-review:** adjust review dialog mobile layout ([#886](https://github.com/sabertazimi/lab/issues/886)) ([d846f70](https://github.com/sabertazimi/lab/commit/d846f7058a0e23eca5149507f93b60a2fb6848e1))
- **m.league-review:** enable review dialog scrollbar ([#887](https://github.com/sabertazimi/lab/issues/887)) ([675158d](https://github.com/sabertazimi/lab/commit/675158d046d8b8ce802423b09b851978eb6c11e2))
- **m.league-review:** reset local value ([#888](https://github.com/sabertazimi/lab/issues/888)) ([ab6cd96](https://github.com/sabertazimi/lab/commit/ab6cd9637c12690d38a4bfd89684c53babbfed9c))
- **m.league-round:** adjust layout for round input buttons ([#893](https://github.com/sabertazimi/lab/issues/893)) ([ea4a08b](https://github.com/sabertazimi/lab/commit/ea4a08b1852a184e2b19bffc784883c24a876419))
- **m.league-round:** chnage round input text ([#892](https://github.com/sabertazimi/lab/issues/892)) ([9c20a45](https://github.com/sabertazimi/lab/commit/9c20a45201136b0e0d50cab8028828ce0249478f))
- **m.league-selection:** change selection text color ([#891](https://github.com/sabertazimi/lab/issues/891)) ([2f57099](https://github.com/sabertazimi/lab/commit/2f57099c3b4d70d418f697c7f38db36b2a4a77f6))
- **m.league-status:** update status colors ([#889](https://github.com/sabertazimi/lab/issues/889)) ([c1e6842](https://github.com/sabertazimi/lab/commit/c1e684254b4469b9453a68976ee273d209eaba11))
- **m.league-toast:** add toaster component ([#882](https://github.com/sabertazimi/lab/issues/882)) ([b737aeb](https://github.com/sabertazimi/lab/commit/b737aeb899875cdece2d48951269795883388f51))

### Features

- **m.league-editor:** implement bubble and floating menu for note editor ([#881](https://github.com/sabertazimi/lab/issues/881)) ([9d0ea2e](https://github.com/sabertazimi/lab/commit/9d0ea2e4f6469a2e53587eb1013e6e8e5350235a))

# [2.1.0](https://github.com/sabertazimi/lab/compare/v2.0.0...v2.1.0) (2025-12-10)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#870](https://github.com/sabertazimi/lab/issues/870)) ([f3d83b1](https://github.com/sabertazimi/lab/commit/f3d83b1804abe28ce0053a20df8111ccdd9be45b))
- **m.league-card:** change player card background color ([#875](https://github.com/sabertazimi/lab/issues/875)) ([59a7e61](https://github.com/sabertazimi/lab/commit/59a7e61d7ca3a821ee886cf880adf7c74cc82548))
- **m.league-round:** change next round logic ([#872](https://github.com/sabertazimi/lab/issues/872)) ([731646c](https://github.com/sabertazimi/lab/commit/731646cc2a50ae287081f4d7c733b1db99537812))
- **m.league-table:** add copy, paste and clear shortcuts ([#874](https://github.com/sabertazimi/lab/issues/874)) ([d5bfe23](https://github.com/sabertazimi/lab/commit/d5bfe23f244ca3fab4713d28e15ef3a114377693))
- **m.league-table:** adjust tab index for review table ([#879](https://github.com/sabertazimi/lab/issues/879)) ([90af8d1](https://github.com/sabertazimi/lab/commit/90af8d15c47cda188341e60ed0d2edb603fad14e))
- **m.league-types:** add more hosetsu types ([#873](https://github.com/sabertazimi/lab/issues/873)) ([e8ba939](https://github.com/sabertazimi/lab/commit/e8ba939f01d145a4767487a8bf6a59514ca478fe))
- **m.league:** migrate from drawer to dialog ([#878](https://github.com/sabertazimi/lab/issues/878)) ([5c120cc](https://github.com/sabertazimi/lab/commit/5c120cc803d149b138dee02dddc40a2c0db36c7b))

### Features

- **m.league-backup:** implement data backup feature ([#880](https://github.com/sabertazimi/lab/issues/880)) ([98c4937](https://github.com/sabertazimi/lab/commit/98c4937648014268bc6848cdcf797b56dfe92b92))
- **m.league-editor:** implement rich text note editor ([#877](https://github.com/sabertazimi/lab/issues/877)) ([08ae796](https://github.com/sabertazimi/lab/commit/08ae796d3e1431df45b5a9b78054243199d7b5d3))
- **m.league-notes:** implement review notes feature ([#876](https://github.com/sabertazimi/lab/issues/876)) ([a9afcfd](https://github.com/sabertazimi/lab/commit/a9afcfdf4a9c4198a8562bda4423f9b7fab06a46))

### Performance Improvements

- [ImgBot] optimize images ([#868](https://github.com/sabertazimi/lab/issues/868)) ([c5cd126](https://github.com/sabertazimi/lab/commit/c5cd126855ed1760ba0af55d0d66a3eb493e64a2))

# [2.0.0](https://github.com/sabertazimi/lab/compare/v1.10.0...v2.0.0) (2025-12-04)

### Bug Fixes

- **m.league:** rectify shadcn/ui config ([293dba9](https://github.com/sabertazimi/lab/commit/293dba99cdfff4acda58e5661d09d4c08657b471))

- feat!(web): add portfolio index page (#866) ([d837d8b](https://github.com/sabertazimi/lab/commit/d837d8b356938ac8157b67e48a7a3326c8278522)), closes [#866](https://github.com/sabertazimi/lab/issues/866)

### BREAKING CHANGES

- - style: format code

# [1.10.0](https://github.com/sabertazimi/lab/compare/v1.9.0...v1.10.0) (2025-12-03)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#853](https://github.com/sabertazimi/lab/issues/853)) ([0e1acdf](https://github.com/sabertazimi/lab/commit/0e1acdf03aa3fbca19b0057366ed414a75607226))
- **deps:** update dependency react-day-picker to ^9.11.3 ([#854](https://github.com/sabertazimi/lab/issues/854)) ([d87e3ea](https://github.com/sabertazimi/lab/commit/d87e3ea63f4b0f6c8abc67594869d86007a5430e))
- **m.league-avatar:** change native `<img>` to avatar component ([#859](https://github.com/sabertazimi/lab/issues/859)) ([4722c75](https://github.com/sabertazimi/lab/commit/4722c75e8def1b12644f9dff59b07ec2a1ebd173))
- **m.league-logo:** add league and teams logo ([#863](https://github.com/sabertazimi/lab/issues/863)) ([9995da8](https://github.com/sabertazimi/lab/commit/9995da80350d5572b146e7a8a9dc5fd3524c5998))
- **m.league-table:** update design for hosetsu input ([#857](https://github.com/sabertazimi/lab/issues/857)) ([12629a3](https://github.com/sabertazimi/lab/commit/12629a3534a7acac7a23533272eeeab84425ba25))
- **m.league:** rectify text color for dark theme ([a47fef5](https://github.com/sabertazimi/lab/commit/a47fef5c42fb5b95d542819bf06e491d1ef0a208))
- **url:** rectify broken vite deploy base url ([#852](https://github.com/sabertazimi/lab/issues/852)) ([2b4f2f6](https://github.com/sabertazimi/lab/commit/2b4f2f62139399e853398f0c7f9f9be4e06434ea))

### Features

- **m.league-background:** add flickering grid to header and footer ([#862](https://github.com/sabertazimi/lab/issues/862)) ([f9d9c99](https://github.com/sabertazimi/lab/commit/f9d9c99d33b6c3011b466c4bf693ce8fcb5f4639))
- **m.league-design:** change to void zero style ([#858](https://github.com/sabertazimi/lab/issues/858)) ([4783b86](https://github.com/sabertazimi/lab/commit/4783b86fac3948cee38af0ba0384a6f88457cc1d))
- **m.league-footer:** add site footer ([#861](https://github.com/sabertazimi/lab/issues/861)) ([3938f80](https://github.com/sabertazimi/lab/commit/3938f8092d7e39b28ea0ceb2907b6dc640df7b87))
- **m.league-SSG:** use react router SSG pre renderer ([#865](https://github.com/sabertazimi/lab/issues/865)) ([33b452a](https://github.com/sabertazimi/lab/commit/33b452a1fa30b9340c166aa2270f532427eb06a2))
- **m.league-theme:** add dark theme support ([#860](https://github.com/sabertazimi/lab/issues/860)) ([6830d2f](https://github.com/sabertazimi/lab/commit/6830d2fa074c33debb287cb9fd23ac60b3c1b99e))
- **m.league:** fetch game schedule and autogenerate team field ([#856](https://github.com/sabertazimi/lab/issues/856)) ([8bc27e2](https://github.com/sabertazimi/lab/commit/8bc27e20d14d22f2240a44c1c4b0d247a9d73613))
- **react-shadcn/ui:** add M.League reviewer app ([#850](https://github.com/sabertazimi/lab/issues/850)) ([b3b7e9b](https://github.com/sabertazimi/lab/commit/b3b7e9b4f83f241dfaadfe6c1d6dd00a92bbd680))

### Performance Improvements

- [ImgBot] optimize images ([#851](https://github.com/sabertazimi/lab/issues/851)) ([4a83e07](https://github.com/sabertazimi/lab/commit/4a83e07826fc867e9c90a8f82d9062de8d9198a2))
