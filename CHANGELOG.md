# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.2.0](https://github.com/sabertazimi/lab/compare/v3.1.0...v3.2.0) (2026-02-01)

### Bug Fixes

- **agent-cli:** correct f-string syntax and enhance agent status display ([#955](https://github.com/sabertazimi/lab/issues/955)) ([2e83e43](https://github.com/sabertazimi/lab/commit/2e83e4332ae5e75f383b2086affef65ded70d9ad))
- **agent-cli:** remove unused `/tasks` command ([2ada3a6](https://github.com/sabertazimi/lab/commit/2ada3a61dabef662cd3612c4a64cdaa7e52df050))

### Features

- **agent-cli:** add config file support ([#953](https://github.com/sabertazimi/lab/issues/953)) ([d16e75c](https://github.com/sabertazimi/lab/commit/d16e75ce50eab2df3eac720b4ea21a8d609857b3))
- **agent-cli:** add graceful Ctrl+C interruption handling ([#956](https://github.com/sabertazimi/lab/issues/956)) ([9386b8f](https://github.com/sabertazimi/lab/commit/9386b8fb037d2e603de5aca923a1d230423c184d))
- **agent-cli:** add slash command system with interactive commands ([#957](https://github.com/sabertazimi/lab/issues/957)) ([faafe13](https://github.com/sabertazimi/lab/commit/faafe13bcbd9f2dd8dc568bd67ef3956c33c31fb))
- **agent-skills:** add Claude Code Plugins integration ([#954](https://github.com/sabertazimi/lab/issues/954)) ([1b73de4](https://github.com/sabertazimi/lab/commit/1b73de4e166b4ac3a5ca682bc5f6e9f355a0e779))
- **agent-tools:** add Glob, Grep, WebSearch, and WebReader tools ([#959](https://github.com/sabertazimi/lab/issues/959)) ([3776f3a](https://github.com/sabertazimi/lab/commit/3776f3af039316a3e090be43a11ad0c199cbfcef))
- **agent-tui:** add Textual TUI with interrupt support ([#958](https://github.com/sabertazimi/lab/issues/958)) ([d51cae3](https://github.com/sabertazimi/lab/commit/d51cae3523a9acdd296aad4b1bdce0258d65dc28))
- **agent:** add creator and email information ([#952](https://github.com/sabertazimi/lab/issues/952)) ([b64d99c](https://github.com/sabertazimi/lab/commit/b64d99c1cef73c68e9121c841d637fef414992a7))

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

### Bug Fixes

- **agent:** add cyber agent identity and normalize line endings ([2ebed0c](https://github.com/sabertazimi/lab/commit/2ebed0c322d9f708ffa14b50cd8c08bc2f028972))

### Features

- **agent-cli:** integrate rich library for terminal output formatting ([#947](https://github.com/sabertazimi/lab/issues/947)) ([6291def](https://github.com/sabertazimi/lab/commit/6291def694fd04a338c95a4419955b0d1a0c9a96))
- **agent-context:** add CLAUDE.md system reminder support ([#946](https://github.com/sabertazimi/lab/issues/946)) ([d4ea0b2](https://github.com/sabertazimi/lab/commit/d4ea0b291b33fdb4cf6885ab0f5b73aa845122a5))
- **agent-skills:** add skill system with SkillLoader ([#950](https://github.com/sabertazimi/lab/issues/950)) ([3f4668e](https://github.com/sabertazimi/lab/commit/3f4668e4c7e4d446ebbd82ca4f2a69627f4ae50f))
- **agent-subagent:** add subagent architecture with Task tool ([#949](https://github.com/sabertazimi/lab/issues/949)) ([11115d1](https://github.com/sabertazimi/lab/commit/11115d1a733e3db98be8944f94d1c4d30e58d394))
- **agent-task:** add task tracking system with TaskManager singleton ([#945](https://github.com/sabertazimi/lab/issues/945)) ([3300927](https://github.com/sabertazimi/lab/commit/330092705459feaa817cfe6156f85f195b4cde64))
- **agent-tools:** improve Windows compatibility for bash tool ([#948](https://github.com/sabertazimi/lab/issues/948)) ([e9185ef](https://github.com/sabertazimi/lab/commit/e9185efb7317da1684893a1faad2004b1fe56f87))
- **agent:** add branding banner and custom semantic theme ([#951](https://github.com/sabertazimi/lab/issues/951)) ([a462230](https://github.com/sabertazimi/lab/commit/a4622308a7bff307ba5eceb4b194a32c8c0010d6))
- **agent:** implement agent loop and tool call ([#943](https://github.com/sabertazimi/lab/issues/943)) ([155e452](https://github.com/sabertazimi/lab/commit/155e452237bb22106aea1b147f7b66c13c86a017))
- **agent:** implement CLI agent with tool loop and REPL ([#940](https://github.com/sabertazimi/lab/issues/940)) ([972345f](https://github.com/sabertazimi/lab/commit/972345f3262046b85e9663c574fb14e5770293e3))
- **bash-agent:** initialize Claude Code learning project ([#938](https://github.com/sabertazimi/lab/issues/938)) ([3e7dd4f](https://github.com/sabertazimi/lab/commit/3e7dd4f86fb00176ca69294d39af751e3b29286a))
- **pnpm:** add python and rust packages to pnpm workspace ([#944](https://github.com/sabertazimi/lab/issues/944)) ([4be9748](https://github.com/sabertazimi/lab/commit/4be97484e842bb72ea65894f99e495ce08c3edc7))
- **python-ruff:** setup ruff linter for Python ([b5426c0](https://github.com/sabertazimi/lab/commit/b5426c0fee2b6a2d5998cf5a567d660eefd475ca))
- **python-type:** setup type hint static check ([#942](https://github.com/sabertazimi/lab/issues/942)) ([e0e1a2c](https://github.com/sabertazimi/lab/commit/e0e1a2cbb8d53ed482eec2ab30e8aa94cdeefc65))
- **python-uv:** setup bash-agent package ([#939](https://github.com/sabertazimi/lab/issues/939)) ([b616855](https://github.com/sabertazimi/lab/commit/b61685522fafac374bc55e76bc15c2c59deb32b3))

### Performance Improvements

- [ImgBot] optimize images ([#937](https://github.com/sabertazimi/lab/issues/937)) ([4f59b84](https://github.com/sabertazimi/lab/commit/4f59b842c4496c14bd45c56670c7190ec0538f10))

# [3.0.0](https://github.com/sabertazimi/lab/compare/v2.5.0...v3.0.0) (2026-01-28)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#929](https://github.com/sabertazimi/lab/issues/929)) ([645c3dc](https://github.com/sabertazimi/lab/commit/645c3dcbfd7315294fdde7778c47f4b6aae545ba))
- **deps:** update dependencies (non-major) ([#933](https://github.com/sabertazimi/lab/issues/933)) ([465b4e4](https://github.com/sabertazimi/lab/commit/465b4e407553663fc9d8359950fef8f56459e18e))
- **portfolio-section:** add radius to site section number ([#925](https://github.com/sabertazimi/lab/issues/925)) ([4494254](https://github.com/sabertazimi/lab/commit/44942548feb5a0bb815e49175f85d8e7d55753de))
- **web-dblp:** rectify source code link ([391496e](https://github.com/sabertazimi/lab/commit/391496e6f3cda7001c40e5ce36114b93d76b22cb))

- feat(rust)!: add rust learning workspace with rustlings, exercism, and docs (#935) ([cfa6854](https://github.com/sabertazimi/lab/commit/cfa6854932c3bf4476e99c39403c621320f89916)), closes [#935](https://github.com/sabertazimi/lab/issues/935)

### Features

- **dblp:** add DBLP search application ([#936](https://github.com/sabertazimi/lab/issues/936)) ([1faf657](https://github.com/sabertazimi/lab/commit/1faf657f95c5ed766ee0d82caa7baa1b1ef0845f))
- **portfolio:** add Rust notes to portfolio ([dc7b574](https://github.com/sabertazimi/lab/commit/dc7b57485799234a7a3acb80118de87d7841a5f7))
- **portfolio:** redesign CSS variable system with comprehensive theme tokens ([#927](https://github.com/sabertazimi/lab/issues/927)) ([d40da95](https://github.com/sabertazimi/lab/commit/d40da95fe6b98298d6561684261da480ff3297cb))

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
- **react-renderer:** update favicon reference to `logo.svg` ([1033374](https://github.com/sabertazimi/lab/commit/103337424efbc7bdc3585a81d8d2b9be535e7d57))

### Features

- **build:** add Vercel deployment support with centralized post-buil… ([#921](https://github.com/sabertazimi/lab/issues/921)) ([1a2bbe5](https://github.com/sabertazimi/lab/commit/1a2bbe5dfbe0c36d18ad2c2d24343a332fe5e61f))
- **m.league-ui:** add consistent border radius styling across UI components ([#919](https://github.com/sabertazimi/lab/issues/919)) ([b700bc8](https://github.com/sabertazimi/lab/commit/b700bc8fd7d3468ad80f1a3fdc039218adc7354c))

### Performance Improvements

- [ImgBot] optimize images ([#923](https://github.com/sabertazimi/lab/issues/923)) ([b5a6a56](https://github.com/sabertazimi/lab/commit/b5a6a56d9543b897a669f8a4f9a23cf2af5bdfd8))

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
- **portfolio:** adjust padding for projects grid ([25b4007](https://github.com/sabertazimi/lab/commit/25b40076a75f3c3a9aba014f2466effe3fe69523))

- feat!(web): add portfolio index page (#866) ([d837d8b](https://github.com/sabertazimi/lab/commit/d837d8b356938ac8157b67e48a7a3326c8278522)), closes [#866](https://github.com/sabertazimi/lab/issues/866)

### Features

- **portfolio:** implement projects portfolio grid ([#867](https://github.com/sabertazimi/lab/issues/867)) ([434ce64](https://github.com/sabertazimi/lab/commit/434ce6410529fda51909803fcd5bb090118b3d75))

### BREAKING CHANGES

- - style: format code

# [1.10.0](https://github.com/sabertazimi/lab/compare/v1.9.0...v1.10.0) (2025-12-03)

### Bug Fixes

- **deps:** remove pnpm patch to vue-tsc ([#724](https://github.com/sabertazimi/lab/issues/724)) ([af9a8a0](https://github.com/sabertazimi/lab/commit/af9a8a0381f7738d74b9105a9f8ab1fd42c7b168)), closes [#716](https://github.com/sabertazimi/lab/issues/716)
- **deps:** update dependencies (non-major) ([#627](https://github.com/sabertazimi/lab/issues/627)) ([f40328c](https://github.com/sabertazimi/lab/commit/f40328cc3ea74af94c18262965da62262daa23af))
- **deps:** update dependencies (non-major) ([#663](https://github.com/sabertazimi/lab/issues/663)) ([9bf6e47](https://github.com/sabertazimi/lab/commit/9bf6e473300598516dc6e7f7723c766cdda5376b))
- **deps:** update dependencies (non-major) ([#669](https://github.com/sabertazimi/lab/issues/669)) ([456ac41](https://github.com/sabertazimi/lab/commit/456ac4127559dcaabc7a4a854b7e3bf08749794e))
- **deps:** update dependencies (non-major) ([#714](https://github.com/sabertazimi/lab/issues/714)) ([25ec0e0](https://github.com/sabertazimi/lab/commit/25ec0e074e2a7491560e4d3245d5da30ad77ca99))
- **deps:** update dependencies (non-major) ([#720](https://github.com/sabertazimi/lab/issues/720)) ([493b82e](https://github.com/sabertazimi/lab/commit/493b82eb399aabe52bdc9568924dfdbb3f83728f))
- **deps:** update dependencies (non-major) ([#728](https://github.com/sabertazimi/lab/issues/728)) ([9d7e790](https://github.com/sabertazimi/lab/commit/9d7e790a58a35c8c89e16cd0c0d58163ce3e07fc))
- **deps:** update dependencies (non-major) ([#729](https://github.com/sabertazimi/lab/issues/729)) ([decb678](https://github.com/sabertazimi/lab/commit/decb67840784bbbf3e9eb284b4aa7e1e18079d18))
- **deps:** update dependencies (non-major) ([#736](https://github.com/sabertazimi/lab/issues/736)) ([47508e2](https://github.com/sabertazimi/lab/commit/47508e2affd2e3651803309ff2d702b2c9c22ca1))
- **deps:** update dependencies (non-major) ([#738](https://github.com/sabertazimi/lab/issues/738)) ([f65ce87](https://github.com/sabertazimi/lab/commit/f65ce872656215a4a4a583653f3882f29074d1dd))
- **deps:** update dependencies (non-major) ([#741](https://github.com/sabertazimi/lab/issues/741)) ([795a964](https://github.com/sabertazimi/lab/commit/795a96460fecf9080f13da27bc761a3da8ee4b6d))
- **deps:** update dependencies (non-major) ([#743](https://github.com/sabertazimi/lab/issues/743)) ([2f27f22](https://github.com/sabertazimi/lab/commit/2f27f226ddb32db24179cef58e393682881e529d))
- **deps:** update dependencies (non-major) ([#746](https://github.com/sabertazimi/lab/issues/746)) ([c710df8](https://github.com/sabertazimi/lab/commit/c710df89c6e07c85a8108b153b68a46f75ad1772))
- **deps:** update dependencies (non-major) ([#750](https://github.com/sabertazimi/lab/issues/750)) ([cd7a42a](https://github.com/sabertazimi/lab/commit/cd7a42af789a852db1395673f0c9f6999ca4723d))
- **deps:** update dependencies (non-major) ([#754](https://github.com/sabertazimi/lab/issues/754)) ([f175bf8](https://github.com/sabertazimi/lab/commit/f175bf8788f4cef74826d3c903da3a1efa6670ef))
- **deps:** update dependencies (non-major) ([#757](https://github.com/sabertazimi/lab/issues/757)) ([2bb693e](https://github.com/sabertazimi/lab/commit/2bb693e1686741bc8c44dfcefa755cbd8fb439f0))
- **deps:** update dependencies (non-major) ([#762](https://github.com/sabertazimi/lab/issues/762)) ([e780f4c](https://github.com/sabertazimi/lab/commit/e780f4ce762ff2800b4d442589e15ce855fcebd2))
- **deps:** update dependencies (non-major) ([#763](https://github.com/sabertazimi/lab/issues/763)) ([b2819d7](https://github.com/sabertazimi/lab/commit/b2819d73483bbecd2609fdc0528daf9e778f0ba3))
- **deps:** update dependencies (non-major) ([#769](https://github.com/sabertazimi/lab/issues/769)) ([73ae1d5](https://github.com/sabertazimi/lab/commit/73ae1d5be0724eda4dc4bc4bc2985e899b9a3225))
- **deps:** update dependencies (non-major) ([#771](https://github.com/sabertazimi/lab/issues/771)) ([0ae3db7](https://github.com/sabertazimi/lab/commit/0ae3db770b1dafdc762059008934dfa124654c06))
- **deps:** update dependencies (non-major) ([#772](https://github.com/sabertazimi/lab/issues/772)) ([4b0668f](https://github.com/sabertazimi/lab/commit/4b0668fff6494265192e10fbcedf8d563dd5397f))
- **deps:** update dependencies (non-major) ([#776](https://github.com/sabertazimi/lab/issues/776)) ([2be976f](https://github.com/sabertazimi/lab/commit/2be976f52e28d46a5bf60b6b1a5761e38aa0225e))
- **deps:** update dependencies (non-major) ([#778](https://github.com/sabertazimi/lab/issues/778)) ([c08df85](https://github.com/sabertazimi/lab/commit/c08df8526a1aae34e19a3ae3da025362da779a55))
- **deps:** update dependencies (non-major) ([#780](https://github.com/sabertazimi/lab/issues/780)) ([412a2f9](https://github.com/sabertazimi/lab/commit/412a2f9d690ff299d33583cb56e99e8afe0992a9))
- **deps:** update dependencies (non-major) ([#782](https://github.com/sabertazimi/lab/issues/782)) ([b178f67](https://github.com/sabertazimi/lab/commit/b178f6719164335ab9405a843dfea0f922746439))
- **deps:** update dependencies (non-major) ([#783](https://github.com/sabertazimi/lab/issues/783)) ([59788be](https://github.com/sabertazimi/lab/commit/59788be43a0036fe1932c516e258797a6e65eea0))
- **deps:** update dependencies (non-major) ([#786](https://github.com/sabertazimi/lab/issues/786)) ([1468ebf](https://github.com/sabertazimi/lab/commit/1468ebf575044c5b67eedc78694cf22355307581))
- **deps:** update dependencies (non-major) ([#792](https://github.com/sabertazimi/lab/issues/792)) ([6a49068](https://github.com/sabertazimi/lab/commit/6a490686fc20393f04804d4490ff4a4d7292c0e1))
- **deps:** update dependencies (non-major) ([#796](https://github.com/sabertazimi/lab/issues/796)) ([df4f761](https://github.com/sabertazimi/lab/commit/df4f761271296377c6486de0baa7f59443d5fccf))
- **deps:** update dependencies (non-major) ([#797](https://github.com/sabertazimi/lab/issues/797)) ([39136ea](https://github.com/sabertazimi/lab/commit/39136ea6adc7647c66b1eb55015d885b0b944106))
- **deps:** update dependencies (non-major) ([#802](https://github.com/sabertazimi/lab/issues/802)) ([4935731](https://github.com/sabertazimi/lab/commit/49357312783bd56e66357ac34175847282802450))
- **deps:** update dependencies (non-major) ([#807](https://github.com/sabertazimi/lab/issues/807)) ([41affc2](https://github.com/sabertazimi/lab/commit/41affc2ddff3828d6c4174ed6b4ff319a1f2757e))
- **deps:** update dependencies (non-major) ([#811](https://github.com/sabertazimi/lab/issues/811)) ([84ed9f6](https://github.com/sabertazimi/lab/commit/84ed9f66bf3f7c3b35dbbfa3f65efadb2d57b88f))
- **deps:** update dependencies (non-major) ([#819](https://github.com/sabertazimi/lab/issues/819)) ([3f238df](https://github.com/sabertazimi/lab/commit/3f238dfe82f0f9211aa78612a4db606d0923da43))
- **deps:** update dependencies (non-major) ([#821](https://github.com/sabertazimi/lab/issues/821)) ([733e40d](https://github.com/sabertazimi/lab/commit/733e40dec33f37d446d7b15a677541fd71196d81))
- **deps:** update dependencies (non-major) ([#823](https://github.com/sabertazimi/lab/issues/823)) ([dfeaafc](https://github.com/sabertazimi/lab/commit/dfeaafca7bd38c57345d7907d0946626a83b903d))
- **deps:** update dependencies (non-major) ([#824](https://github.com/sabertazimi/lab/issues/824)) ([9caa4d8](https://github.com/sabertazimi/lab/commit/9caa4d8d22c3a3e346fe18eba6d31b323ad1c896))
- **deps:** update dependencies (non-major) ([#827](https://github.com/sabertazimi/lab/issues/827)) ([f7f4ec5](https://github.com/sabertazimi/lab/commit/f7f4ec5c25769f2113c453b4b64ef824bd3d01fe))
- **deps:** update dependencies (non-major) ([#829](https://github.com/sabertazimi/lab/issues/829)) ([8239258](https://github.com/sabertazimi/lab/commit/8239258951f4fe58bbac9a28c9a4e36286861607))
- **deps:** update dependencies (non-major) ([#833](https://github.com/sabertazimi/lab/issues/833)) ([59a0ace](https://github.com/sabertazimi/lab/commit/59a0ace102d892db917d07eb023f30d631ad30ec))
- **deps:** update dependencies (non-major) ([#836](https://github.com/sabertazimi/lab/issues/836)) ([4a0405c](https://github.com/sabertazimi/lab/commit/4a0405c254177bbcdc16a166d6b3697906200f63))
- **deps:** update dependencies (non-major) ([#838](https://github.com/sabertazimi/lab/issues/838)) ([06f990e](https://github.com/sabertazimi/lab/commit/06f990e1dc4b015f8ff663b543755a97ed1b816f))
- **deps:** update dependencies (non-major) ([#839](https://github.com/sabertazimi/lab/issues/839)) ([6d5d0bc](https://github.com/sabertazimi/lab/commit/6d5d0bc5394b968aeb18af870cc0a76e59f8206c))
- **deps:** update dependencies (non-major) ([#849](https://github.com/sabertazimi/lab/issues/849)) ([4786c2c](https://github.com/sabertazimi/lab/commit/4786c2c35f1a1ca0408c5238c92c6fc341d626b5))
- **deps:** update dependencies (non-major) ([#853](https://github.com/sabertazimi/lab/issues/853)) ([0e1acdf](https://github.com/sabertazimi/lab/commit/0e1acdf03aa3fbca19b0057366ed414a75607226))
- **deps:** update dependency @types/node to ^22.15.34 ([#790](https://github.com/sabertazimi/lab/issues/790)) ([ec882fd](https://github.com/sabertazimi/lab/commit/ec882fd11c9ac4bfc05505b2e155e2deac882d9b))
- **deps:** update dependency @types/node to ^22.16.5 ([#800](https://github.com/sabertazimi/lab/issues/800)) ([fc43b73](https://github.com/sabertazimi/lab/commit/fc43b738c10e0b205a4f4bf56929da099516a58e))
- **deps:** update dependency @types/node to v24 ([#845](https://github.com/sabertazimi/lab/issues/845)) ([06f48e3](https://github.com/sabertazimi/lab/commit/06f48e3cd5b3bcea0fdb07cca1c03dcab37f900b))
- **deps:** update dependency @unhead/vue to ^1.11.1 ([#691](https://github.com/sabertazimi/lab/issues/691)) ([227e384](https://github.com/sabertazimi/lab/commit/227e3841595d88d915554acdf2cf6184d7d5cf3f))
- **deps:** update dependency @unhead/vue to ^1.11.3 ([#696](https://github.com/sabertazimi/lab/issues/696)) ([3bb884c](https://github.com/sabertazimi/lab/commit/3bb884ceed462149c40d1859749038078202f7e1))
- **deps:** update dependency @unhead/vue to ^1.9.16 ([#672](https://github.com/sabertazimi/lab/issues/672)) ([e4fe91d](https://github.com/sabertazimi/lab/commit/e4fe91d7d9c0c67379d76c6cce292440881189c2))
- **deps:** update dependency @unhead/vue to ^2.0.12 ([#795](https://github.com/sabertazimi/lab/issues/795)) ([2c1421e](https://github.com/sabertazimi/lab/commit/2c1421e27123609ff2f446488ab1fa0d4ac48ed4))
- **deps:** update dependency @unhead/vue to v2 ([#764](https://github.com/sabertazimi/lab/issues/764)) ([fdf28e1](https://github.com/sabertazimi/lab/commit/fdf28e1e075d257f909d4f0404718fc376415354))
- **deps:** update dependency @vueuse/core to v14 ([#844](https://github.com/sabertazimi/lab/issues/844)) ([8c268cb](https://github.com/sabertazimi/lab/commit/8c268cb193cc1839b581ae1115a5f683f581f425))
- **deps:** update dependency echarts to v6 ([#810](https://github.com/sabertazimi/lab/issues/810)) ([bf2da80](https://github.com/sabertazimi/lab/commit/bf2da807e232af3f9ad17fa2ba91f25d47d1252e))
- **deps:** update dependency element-plus to ^2.10.1 ([#781](https://github.com/sabertazimi/lab/issues/781)) ([ea91ebf](https://github.com/sabertazimi/lab/commit/ea91ebfe98b75ab5f9d139505ddc76e87eef6114))
- **deps:** update dependency element-plus to ^2.11.1 ([#822](https://github.com/sabertazimi/lab/issues/822)) ([6bd2738](https://github.com/sabertazimi/lab/commit/6bd2738e069e99ce045013ec1f8d469648b55685))
- **deps:** update dependency element-plus to ^2.7.1 ([#638](https://github.com/sabertazimi/lab/issues/638)) ([b0587bc](https://github.com/sabertazimi/lab/commit/b0587bcbc2db1b2ace57ff02e6e2f44c43772e76))
- **deps:** update dependency element-plus to ^2.9.9 ([#773](https://github.com/sabertazimi/lab/issues/773)) ([7beaceb](https://github.com/sabertazimi/lab/commit/7beaceb4870b76b47e3a627ff71b3a5e35319494))
- **deps:** update dependency nanoid to ^5.1.2 ([#752](https://github.com/sabertazimi/lab/issues/752)) ([89e2812](https://github.com/sabertazimi/lab/commit/89e281206ef89383c3472bbc2ac6d5d8a1462129))
- **deps:** update dependency nanoid to ^5.1.4 ([#761](https://github.com/sabertazimi/lab/issues/761)) ([1aff3b4](https://github.com/sabertazimi/lab/commit/1aff3b4ef517e6ff39983874f34a551ae419008e))
- **deps:** update dependency pinia to v3 ([#747](https://github.com/sabertazimi/lab/issues/747)) ([cb593bc](https://github.com/sabertazimi/lab/commit/cb593bc766c0ad17f01a731b32366778c4e9a38a))
- **deps:** update dependency react-day-picker to ^9.11.3 ([#854](https://github.com/sabertazimi/lab/issues/854)) ([d87e3ea](https://github.com/sabertazimi/lab/commit/d87e3ea63f4b0f6c8abc67594869d86007a5430e))
- **deps:** update dependency vue to ^3.5.11 ([#702](https://github.com/sabertazimi/lab/issues/702)) ([aecee85](https://github.com/sabertazimi/lab/commit/aecee85c8ee658d99054118afd77f179618d3547))
- **deps:** update dependency vue-echarts to v7 ([#779](https://github.com/sabertazimi/lab/issues/779)) ([200fa72](https://github.com/sabertazimi/lab/commit/200fa723a2db68caa3e3571829136d5bb9f7db77))
- **deps:** update dependency vue-echarts to v8 ([#831](https://github.com/sabertazimi/lab/issues/831)) ([841190b](https://github.com/sabertazimi/lab/commit/841190b5c4f1b4c34ffe9d222a7fc514db5709b9))
- **deps:** update dependency vue-i18n to ^10.0.2 ([#698](https://github.com/sabertazimi/lab/issues/698)) ([9e44560](https://github.com/sabertazimi/lab/commit/9e445601733da0feb0a2cdd3ac48fa62c248d84c))
- **deps:** update dependency vue-i18n to ^10.0.3 ([#700](https://github.com/sabertazimi/lab/issues/700)) ([fa4d25d](https://github.com/sabertazimi/lab/commit/fa4d25d759011528349403e6a95212914dd07726))
- **deps:** update dependency vue-i18n to ^10.0.4 ([#703](https://github.com/sabertazimi/lab/issues/703)) ([ed3bdea](https://github.com/sabertazimi/lab/commit/ed3bdea8425ba5082c5a2f1612725f2b7c69f3eb))
- **deps:** update dependency vue-i18n to ^11.1.3 ([#767](https://github.com/sabertazimi/lab/issues/767)) ([02cc678](https://github.com/sabertazimi/lab/commit/02cc6780e5999f76c42c20f917aed7701e712915))
- **deps:** update dependency vue-i18n to ^11.1.7 ([#785](https://github.com/sabertazimi/lab/issues/785)) ([ed9e5fe](https://github.com/sabertazimi/lab/commit/ed9e5fed4225645ac83c025ac0bedc808893307d))
- **deps:** update dependency vue-i18n to ^9.12.1 ([#634](https://github.com/sabertazimi/lab/issues/634)) ([ced9988](https://github.com/sabertazimi/lab/commit/ced99884cbefcd55fefe66804b315ff6740d3a51))
- **deps:** update dependency vue-i18n to ^9.13.1 ([#640](https://github.com/sabertazimi/lab/issues/640)) ([7f5942f](https://github.com/sabertazimi/lab/commit/7f5942fdb3023ad2ea21d04e64470e28e55cb966))
- **deps:** update dependency vue-i18n to v10 ([#692](https://github.com/sabertazimi/lab/issues/692)) ([faabf20](https://github.com/sabertazimi/lab/commit/faabf2057e8b886c6f5eaa988286f1c8b2319f57))
- **deps:** update dependency vue-i18n to v11 ([#726](https://github.com/sabertazimi/lab/issues/726)) ([90f60f8](https://github.com/sabertazimi/lab/commit/90f60f8534a10681553f11486854a8c7d7c2c2c2))
- **deps:** update dependency web-vitals to v4 ([#649](https://github.com/sabertazimi/lab/issues/649)) ([28257ea](https://github.com/sabertazimi/lab/commit/28257ead46e445caa9a90b7867e77a0ef29b44e1))
- **m.league-avatar:** change native `<img>` to avatar component ([#859](https://github.com/sabertazimi/lab/issues/859)) ([4722c75](https://github.com/sabertazimi/lab/commit/4722c75e8def1b12644f9dff59b07ec2a1ebd173))
- **m.league-logo:** add league and teams logo ([#863](https://github.com/sabertazimi/lab/issues/863)) ([9995da8](https://github.com/sabertazimi/lab/commit/9995da80350d5572b146e7a8a9dc5fd3524c5998))
- **m.league-table:** update design for hosetsu input ([#857](https://github.com/sabertazimi/lab/issues/857)) ([12629a3](https://github.com/sabertazimi/lab/commit/12629a3534a7acac7a23533272eeeab84425ba25))
- **m.league:** rectify text color for dark theme ([a47fef5](https://github.com/sabertazimi/lab/commit/a47fef5c42fb5b95d542819bf06e491d1ef0a208))
- **react:** remove unused web-vitals package ([#650](https://github.com/sabertazimi/lab/issues/650)) ([cdc60a2](https://github.com/sabertazimi/lab/commit/cdc60a282c6b850ff392b27aabc29b3c418d953d))
- **url:** rectify broken vite deploy base url ([#852](https://github.com/sabertazimi/lab/issues/852)) ([2b4f2f6](https://github.com/sabertazimi/lab/commit/2b4f2f62139399e853398f0c7f9f9be4e06434ea))
- **vue-echarts:** add scatter symbol ([427eef8](https://github.com/sabertazimi/lab/commit/427eef859946876cb863e30052289edc7a0f7483))
- **vue-echarts:** rectify base url ([b3a416c](https://github.com/sabertazimi/lab/commit/b3a416c03ccad1e022584ed26210c3b8ac03f212))

### Features

- **m.league-background:** add flickering grid to header and footer ([#862](https://github.com/sabertazimi/lab/issues/862)) ([f9d9c99](https://github.com/sabertazimi/lab/commit/f9d9c99d33b6c3011b466c4bf693ce8fcb5f4639))
- **m.league-design:** change to void zero style ([#858](https://github.com/sabertazimi/lab/issues/858)) ([4783b86](https://github.com/sabertazimi/lab/commit/4783b86fac3948cee38af0ba0384a6f88457cc1d))
- **m.league-footer:** add site footer ([#861](https://github.com/sabertazimi/lab/issues/861)) ([3938f80](https://github.com/sabertazimi/lab/commit/3938f8092d7e39b28ea0ceb2907b6dc640df7b87))
- **m.league-SSG:** use react router SSG pre renderer ([#865](https://github.com/sabertazimi/lab/issues/865)) ([33b452a](https://github.com/sabertazimi/lab/commit/33b452a1fa30b9340c166aa2270f532427eb06a2))
- **m.league-theme:** add dark theme support ([#860](https://github.com/sabertazimi/lab/issues/860)) ([6830d2f](https://github.com/sabertazimi/lab/commit/6830d2fa074c33debb287cb9fd23ac60b3c1b99e))
- **m.league:** fetch game schedule and autogenerate team field ([#856](https://github.com/sabertazimi/lab/issues/856)) ([8bc27e2](https://github.com/sabertazimi/lab/commit/8bc27e20d14d22f2240a44c1c4b0d247a9d73613))
- **react-shadcn/ui:** add M.League reviewer app ([#850](https://github.com/sabertazimi/lab/issues/850)) ([b3b7e9b](https://github.com/sabertazimi/lab/commit/b3b7e9b4f83f241dfaadfe6c1d6dd00a92bbd680))
- **vue-echarts:** echarts dashboard ([#777](https://github.com/sabertazimi/lab/issues/777)) ([8c602d8](https://github.com/sabertazimi/lab/commit/8c602d80571fbd701c23957c2357ce50863a1507))

### Performance Improvements

- [ImgBot] optimize images ([#851](https://github.com/sabertazimi/lab/issues/851)) ([4a83e07](https://github.com/sabertazimi/lab/commit/4a83e07826fc867e9c90a8f82d9062de8d9198a2))

# [1.9.0](https://github.com/sabertazimi/lab/compare/v1.8.0...v1.9.0) (2024-04-01)

### Bug Fixes

- add logic for dahai after claim ([#606](https://github.com/sabertazimi/lab/issues/606)) ([58eb700](https://github.com/sabertazimi/lab/commit/58eb700ba70135abe5dd976d1bd6723e7a1a325a))
- **deps:** update dependencies (non-major) ([#504](https://github.com/sabertazimi/lab/issues/504)) ([86827fb](https://github.com/sabertazimi/lab/commit/86827fbdec15bac30b8270d553a286bc5fe09bb5))
- **deps:** update dependency @unhead/vue to ^1.8.20 ([#610](https://github.com/sabertazimi/lab/issues/610)) ([9406d0d](https://github.com/sabertazimi/lab/commit/9406d0d47a6159bc82ad475b4dbdcdd0d7db8300))
- **deps:** update dependency @unhead/vue to ^1.9.4 ([#619](https://github.com/sabertazimi/lab/issues/619)) ([8084314](https://github.com/sabertazimi/lab/commit/8084314c9cdae592c56927c56b197d8f84bdf94c))
- **deps:** update dependency core-js to ^3.30.2 ([#488](https://github.com/sabertazimi/lab/issues/488)) ([708ca5f](https://github.com/sabertazimi/lab/commit/708ca5fc27bdb641cd014ce0f6017219314baaf5))
- **deps:** update dependency core-js to ^3.35.1 ([#585](https://github.com/sabertazimi/lab/issues/585)) ([6abf92e](https://github.com/sabertazimi/lab/commit/6abf92eea3fa6eb38258a76f8e63053b59147524))
- **deps:** update dependency nanoid to ^4.0.1 ([#445](https://github.com/sabertazimi/lab/issues/445)) ([97b3884](https://github.com/sabertazimi/lab/commit/97b38840315185aa94b5e71f421e203c9a560573))
- **deps:** update dependency nanoid to ^4.0.2 ([#473](https://github.com/sabertazimi/lab/issues/473)) ([17e6ee5](https://github.com/sabertazimi/lab/commit/17e6ee51b184d1f6cf42550ae456a75a1b8876e2))
- **deps:** update dependency nanoid to v5 ([#526](https://github.com/sabertazimi/lab/issues/526)) ([43b8887](https://github.com/sabertazimi/lab/commit/43b888738e4f7baf1e937bd61dbd8e766f93102e))
- **deps:** update dependency snabbdom to ^3.6.0 ([#583](https://github.com/sabertazimi/lab/issues/583)) ([dffcf3a](https://github.com/sabertazimi/lab/commit/dffcf3ab630bce82518df54b76dc933066d0210c))
- **mortal:** rectify build prefix path bug ([#604](https://github.com/sabertazimi/lab/issues/604)) ([89287be](https://github.com/sabertazimi/lab/commit/89287bede4bff1ad0163c2608721f567adcdd27b))
- switch to eslint flat config ([#607](https://github.com/sabertazimi/lab/issues/607)) ([7fecdae](https://github.com/sabertazimi/lab/commit/7fecdae1f27a4c636943b87eb2f2efa0ae192213))

### Features

- **mortal:** add Mortal GUI Vue project ([#602](https://github.com/sabertazimi/lab/issues/602)) ([62baa1e](https://github.com/sabertazimi/lab/commit/62baa1edea6eca0ab331cf9c221953824854199a))
- show expected and actual choices ([#605](https://github.com/sabertazimi/lab/issues/605)) ([d56c994](https://github.com/sabertazimi/lab/commit/d56c9941d919270c337a1623348350dd09348b71))

# [1.8.0](https://github.com/sabertazimi/lab/compare/v1.7.1...v1.8.0) (2022-08-29)

### Bug Fixes

- **deps:** update dependency nanoid to v4 ([#347](https://github.com/sabertazimi/lab/issues/347)) ([9260f1f](https://github.com/sabertazimi/lab/commit/9260f1fd76825fb577e25593a632ef93c85fe6cc))
- **deps:** update dependency web-vitals to v3 ([#376](https://github.com/sabertazimi/lab/issues/376)) ([b3dd57f](https://github.com/sabertazimi/lab/commit/b3dd57f8259cdb1d42a51c0f9d33d62dd4fb6d0c))
- **vue-challenges:** `customRef` API ([7a85256](https://github.com/sabertazimi/lab/commit/7a8525660cacd6f5260917b31191a8a65bc22151))
- **vue-challenges:** `effectScope()` API ([8c6d57d](https://github.com/sabertazimi/lab/commit/8c6d57d8bea38cdebe71d8566ae395fc9e8436f4))
- **vue-challenges:** `h()` render function ([20c12c4](https://github.com/sabertazimi/lab/commit/20c12c44711a467f94708b096c1e14518b03105e))
- **vue-challenges:** `markRaw` and `toRaw` API ([9497399](https://github.com/sabertazimi/lab/commit/94973991a7216a0656f8dbb296835d7f56352350))
- **vue-challenges:** `nextTick()` API ([e3e5683](https://github.com/sabertazimi/lab/commit/e3e56837131ea7ba2a10178d8cc13a788d1d3520))
- **vue-challenges:** `v-bind()` dynamic CSS values ([763d0fa](https://github.com/sabertazimi/lab/commit/763d0fae8d7ac042d9cf86100ee2ef6abd48585e))
- **vue-challenges:** `v-once` directive ([b883eb3](https://github.com/sabertazimi/lab/commit/b883eb3bde4ff5c3a03392586f259bb297b35100))
- **vue-challenges:** `watch` promise statement ([9496211](https://github.com/sabertazimi/lab/commit/9496211f5c01fb455f7b3aab7dd2a458d47e9bd6))
- **vue-challenges:** complete custom directive modifier challenge ([#374](https://github.com/sabertazimi/lab/issues/374)) ([dca4e73](https://github.com/sabertazimi/lab/commit/dca4e73d3641dd03071ee869d0eba24087180f47))
- **vue-challenges:** complete losing reactivity challenge ([835c5f7](https://github.com/sabertazimi/lab/commit/835c5f7b931d5d487456d652cfb72e919d3cdc11))
- **vue-challenges:** complete ref family challenge ([b25f88f](https://github.com/sabertazimi/lab/commit/b25f88f48036d5f80808025d1a34a272be890e61))
- **vue-challenges:** complete watch family ([0fc1638](https://github.com/sabertazimi/lab/commit/0fc1638cd9aed1b2123181cd0005e3d85c123878))
- **vue-challenges:** composable function ([3f83644](https://github.com/sabertazimi/lab/commit/3f83644366fe6ccdeef2cfb5e1fb90cfc24e8849))
- **vue-challenges:** composable function ([4968f4b](https://github.com/sabertazimi/lab/commit/4968f4bd98d72ec82c478cbafa9c68e1037b6536))
- **vue-challenges:** composable functions ([cf97f4e](https://github.com/sabertazimi/lab/commit/cf97f4e93302c86d4c9f12c829afabab0593400d))
- **vue-challenges:** custom debounce ref ([0ec39e6](https://github.com/sabertazimi/lab/commit/0ec39e674726eee9300f5067e680553f54ba490c))
- **vue-challenges:** custom directive ([1fa5f47](https://github.com/sabertazimi/lab/commit/1fa5f47841d1c9ca9823a873186d46c73f682453))
- **vue-challenges:** custom watch effect directive ([972cc9f](https://github.com/sabertazimi/lab/commit/972cc9f18be6587f1de946acf053b0ccc72837b7))
- **vue-challenges:** debounce click custom directive ([70d9188](https://github.com/sabertazimi/lab/commit/70d9188c50b9563ddf28843ac814b883a69158cf))
- **vue-challenges:** define custom web components ([962baee](https://github.com/sabertazimi/lab/commit/962baeec2d23c4e0751df6f1c27eff3f6d70a12c))
- **vue-challenges:** event `.stop` modifer ([dc4a1d8](https://github.com/sabertazimi/lab/commit/dc4a1d8a73e690d6fc224eda8b3797f2ade6bbb7))
- **vue-challenges:** event key modifiers ([888f734](https://github.com/sabertazimi/lab/commit/888f73440a43eb24198dff9ca25a6fd2e382b2fd))
- **vue-challenges:** functional component helper `h()` ([5f1bdec](https://github.com/sabertazimi/lab/commit/5f1bdece6b8fe3d91fa253071eb6938430471889))
- **vue-challenges:** global style selector `:global()` ([784f783](https://github.com/sabertazimi/lab/commit/784f783b320304239aad1c9bc9918a38658e73cc))
- **vue-challenges:** lifecycle composition API ([2719391](https://github.com/sabertazimi/lab/commit/2719391a95fb5fc9b0e33d4e6c74e09db02cdb03))
- **vue-challenges:** minimal model binding directive ([3e42f8a](https://github.com/sabertazimi/lab/commit/3e42f8a4b2e740ac3b6ac63a359cf2c7f4c99282))
- **vue-challenges:** props validation ([feadcf3](https://github.com/sabertazimi/lab/commit/feadcf37a956ca0f5ffc1533e17f5e8191e71bc7))
- **vue-challenges:** provide and inject API ([fb73ef0](https://github.com/sabertazimi/lab/commit/fb73ef0f5f49247ed035b06a37335222a21c7710))
- **vue-challenges:** shallow ref ([6ba75e1](https://github.com/sabertazimi/lab/commit/6ba75e135f31a3e9d13de3099fc48f622f928551))
- **vue-challenges:** teleport built-in component ([0991787](https://github.com/sabertazimi/lab/commit/0991787daca912fe4511e786be2359f854b55f69))
- **vue-challenges:** tree component ([c2c077b](https://github.com/sabertazimi/lab/commit/c2c077b3f2dfbea7c338f0b668a385aca38a1553))
- **vue-challenges:** writable computed value ([772b53d](https://github.com/sabertazimi/lab/commit/772b53deb33972f035b944f613223a7b94e58d12))

### Features

- **vue-challenges:** start vuejs challenges project ([#372](https://github.com/sabertazimi/lab/issues/372)) ([b480e40](https://github.com/sabertazimi/lab/commit/b480e40429367133d0626aa86a8afcbfc1eab05b))

## [1.7.1](https://github.com/sabertazimi/lab/compare/v1.7.0...v1.7.1) (2022-05-27)

### Bug Fixes

- **deps:** update react monorepo to v18 ([#306](https://github.com/sabertazimi/lab/issues/306)) ([035a11d](https://github.com/sabertazimi/lab/commit/035a11d4730874e23463a8b01a79f94128ed3ae0))
- **react-renderer:** implement React 18 style renderer ([#302](https://github.com/sabertazimi/lab/issues/302)) ([4b3f8a6](https://github.com/sabertazimi/lab/commit/4b3f8a6af95096df782b08569c898a741cf3da98))

# [1.7.0](https://github.com/sabertazimi/lab/compare/v1.6.1...v1.7.0) (2022-03-24)

### Bug Fixes

- **deps:** update dependency core-js to ^3.18.2 ([#84](https://github.com/sabertazimi/lab/issues/84)) ([07013f9](https://github.com/sabertazimi/lab/commit/07013f9c1c7e67b618f89e106ae4ae18c066faa4))
- **deps:** update dependency core-js to ^3.18.3 ([#105](https://github.com/sabertazimi/lab/issues/105)) ([5aed5e4](https://github.com/sabertazimi/lab/commit/5aed5e4f541fa0f94db7f8a98563e6c33e50c52c))
- **deps:** update dependency core-js to ^3.19.0 ([#138](https://github.com/sabertazimi/lab/issues/138)) ([5ccfd48](https://github.com/sabertazimi/lab/commit/5ccfd4875194e4ff18eb302284344884f38c3089))
- **deps:** update dependency core-js to ^3.19.1 ([#143](https://github.com/sabertazimi/lab/issues/143)) ([df7fb0f](https://github.com/sabertazimi/lab/commit/df7fb0f4ab09aeecf12ca978d02a31223f3b561a))
- **deps:** update dependency core-js to ^3.19.2 ([#175](https://github.com/sabertazimi/lab/issues/175)) ([603cd7a](https://github.com/sabertazimi/lab/commit/603cd7a085b6a1a17893550e9aeb8fce0372815a))
- **deps:** update dependency core-js to ^3.19.3 ([#189](https://github.com/sabertazimi/lab/issues/189)) ([1583028](https://github.com/sabertazimi/lab/commit/15830283ddbe042e8bc90af1d324bcf874c4b294))
- **deps:** update dependency core-js to ^3.20.0 ([#203](https://github.com/sabertazimi/lab/issues/203)) ([06403da](https://github.com/sabertazimi/lab/commit/06403dab058d2e11d72188264d22df1faf1910e1))
- **deps:** update dependency core-js to ^3.20.1 ([#208](https://github.com/sabertazimi/lab/issues/208)) ([ce00fa6](https://github.com/sabertazimi/lab/commit/ce00fa6053f894b8b3fc7beeafe270ec8352b8ee))
- **deps:** update dependency core-js to ^3.20.2 ([#219](https://github.com/sabertazimi/lab/issues/219)) ([f152240](https://github.com/sabertazimi/lab/commit/f1522403e4a1a4ae8696a4930fe55b4757871d63))
- **deps:** update dependency core-js to ^3.21.0 ([#246](https://github.com/sabertazimi/lab/issues/246)) ([e855db1](https://github.com/sabertazimi/lab/commit/e855db1d9d4f80290eed4ffff013fd7ccd303ccc))
- **deps:** update dependency core-js to ^3.21.1 ([#256](https://github.com/sabertazimi/lab/issues/256)) ([a6c8ec0](https://github.com/sabertazimi/lab/commit/a6c8ec0e439d2a72f0664f7ecc5c23ff06ae5313))
- **deps:** update dependency nanoid to ^3.1.29 ([#85](https://github.com/sabertazimi/lab/issues/85)) ([7bb1a51](https://github.com/sabertazimi/lab/commit/7bb1a513bfd8de7ad93f64bc1f0695a36b6c58ad))
- **deps:** update dependency nanoid to ^3.1.30 ([#106](https://github.com/sabertazimi/lab/issues/106)) ([6223621](https://github.com/sabertazimi/lab/commit/6223621d796e20d623073422a09944914761973f))
- **deps:** update dependency nanoid to ^3.2.0 ([#238](https://github.com/sabertazimi/lab/issues/238)) ([82e46c5](https://github.com/sabertazimi/lab/commit/82e46c52cd61f8fef09cc00702ecf8efb2717726))
- **deps:** update dependency nanoid to ^3.3.1 ([#259](https://github.com/sabertazimi/lab/issues/259)) ([378f02d](https://github.com/sabertazimi/lab/commit/378f02db78f04bc74f82add875304742495c728e))
- **deps:** update dependency vue-router to ^4.0.13 ([#276](https://github.com/sabertazimi/lab/issues/276)) ([b1c285d](https://github.com/sabertazimi/lab/commit/b1c285d93ee0155f1e77421dd783e5981c564e00))
- **deps:** update dependency vue-router to ^4.0.14 ([#286](https://github.com/sabertazimi/lab/issues/286)) ([87b62d4](https://github.com/sabertazimi/lab/commit/87b62d499018c7d6e4901271866039739ecd16f7))
- **deps:** update dependency web-vitals to ^2.1.1 ([#86](https://github.com/sabertazimi/lab/issues/86)) ([90659cd](https://github.com/sabertazimi/lab/commit/90659cdfe70da8f66608950f750ec456966176fa))
- **deps:** update dependency web-vitals to ^2.1.2 ([#107](https://github.com/sabertazimi/lab/issues/107)) ([a0ef5fa](https://github.com/sabertazimi/lab/commit/a0ef5fa53dbb32ed48b57c56445aa4fe50e83554))
- **deps:** update dependency web-vitals to ^2.1.3 ([#226](https://github.com/sabertazimi/lab/issues/226)) ([8aec682](https://github.com/sabertazimi/lab/commit/8aec68268bd349264c5e0f47a2f3fa6c54272d2d))
- **deps:** update dependency web-vitals to ^2.1.4 ([#239](https://github.com/sabertazimi/lab/issues/239)) ([6cddf0f](https://github.com/sabertazimi/lab/commit/6cddf0f98ba4745468877de39d7c0f3f7f966e34))
- **react-renderer:** attach event listeners to DOM nodes ([fead3e6](https://github.com/sabertazimi/lab/commit/fead3e6939ca97c2dac3fca8aaf297f1e8a9fb5b))
- **react-renderer:** filter undefined props ([614d8aa](https://github.com/sabertazimi/lab/commit/614d8aaf881e4d655514add4cbd057bde9820335))
- **react-renderer:** generate root host context ([5b90222](https://github.com/sabertazimi/lab/commit/5b9022213c859dfcd5a75d2af54396e9d573f90d))
- **react-renderer:** implement basic HostConfig API ([3f7c3cc](https://github.com/sabertazimi/lab/commit/3f7c3cc7e89005e2aa53cca38b07dace609bd868))
- **react-renderer:** implement commit phase functions ([8071bd0](https://github.com/sabertazimi/lab/commit/8071bd0e5926ad06f30db36084a69747d3241402))
- **react-renderer:** implemented default renderer behavior ([09b0ff8](https://github.com/sabertazimi/lab/commit/09b0ff804ee6389a5be26c9b0948ffff5dd32e30))
- **react-renderer:** process `svg` element ([de32e84](https://github.com/sabertazimi/lab/commit/de32e846709b53224f6e3acc3ab4b1a35d0b3182))
- **react-renderer:** render svg tags with `createElementNS` function ([111d856](https://github.com/sabertazimi/lab/commit/111d856e432ba1d6390affeaf842be6c47c9ad2e))
- **react-renderer:** update function signatures ([40f91dc](https://github.com/sabertazimi/lab/commit/40f91dce8773496aa897b21a676e7471d8d52f53))
- **react-renderer:** update function signatures ([7524f73](https://github.com/sabertazimi/lab/commit/7524f735756b8bdb1a5e0ec9a866d00c2d20e494))
- **vue-basis:** rectify building prefix path ([#270](https://github.com/sabertazimi/lab/issues/270)) ([de38664](https://github.com/sabertazimi/lab/commit/de38664e59db3537063cba8a45271e1db336b896))
- **vue-design:** update vitrual DOM and apply to DOM ([#271](https://github.com/sabertazimi/lab/issues/271)) ([8c81318](https://github.com/sabertazimi/lab/commit/8c813187236e6b3594bb8663d6f38498d95c3964))

### Features

- **react-renderer:** setup custom React renderer ([#295](https://github.com/sabertazimi/lab/issues/295)) ([953c221](https://github.com/sabertazimi/lab/commit/953c221b5171a65605d073e28be59924705260a5))
- **vue-design:** setup demo for vue design learning ([#269](https://github.com/sabertazimi/lab/issues/269)) ([4bbb62e](https://github.com/sabertazimi/lab/commit/4bbb62efa32436f4d59a8fb06b9dbd6809843c48))

## [1.6.1](https://github.com/sabertazimi/lab/compare/v1.6.0...v1.6.1) (2021-10-04)

### Bug Fixes

- **deps:** update dependency core-js to ^3.18.1 ([#71](https://github.com/sabertazimi/lab/issues/71)) ([1f7d2ea](https://github.com/sabertazimi/lab/commit/1f7d2ea7999d9cbc808e4c44da03a3a591cf1011))
- **Vue-composition:** create reuseable composition function ([6a93a73](https://github.com/sabertazimi/lab/commit/6a93a73e5ebb6f94f3fc7cb65c6c442e51ecb3c4))
- **Vue-tailwind:** polish up button tailwind component ([4029014](https://github.com/sabertazimi/lab/commit/40290144d65028f639fb93d69b42d1ad867d185b))
- **Vue-trello:** add drop zone on task item ([8c24556](https://github.com/sabertazimi/lab/commit/8c24556a4d330f8a2381d14bdca1dc2664ffe5c6))
- **Vue-trello:** change rounded style to block edge style ([6f632d0](https://github.com/sabertazimi/lab/commit/6f632d0b345ef03d092550ddf2bc915e71e1b2d2))
- **Vue-trello:** implement add and delete column feature ([31c5751](https://github.com/sabertazimi/lab/commit/31c5751c1b80b36a6240a44f3565ec4bdeed7d76))
- **Vue-trello:** implement column drag feature ([153ed90](https://github.com/sabertazimi/lab/commit/153ed904183ac1b216c490f4c2b906a556f8726f))
- **Vue-trello:** implement task drag feature ([aec1bec](https://github.com/sabertazimi/lab/commit/aec1bec865633b481a89b6c727ae6cd8204d7485))
- **Vue-trello:** implement task drag on same column ([a49cf74](https://github.com/sabertazimi/lab/commit/a49cf74adbfe3390fd0ba5ec4704fe5b2578b934))
- **Vue-trello:** normalize event modifier for nesting draggable elements ([762a40a](https://github.com/sabertazimi/lab/commit/762a40a39f453758ab163257d456852ae9ca26e4))
- **Vue-trello:** re-style column creatation input widget ([fbe0a1c](https://github.com/sabertazimi/lab/commit/fbe0a1c20a1863e05ff565bf4ddc09f3b9979d76))
- **Vue-trello:** rectify clickable zone ([db49088](https://github.com/sabertazimi/lab/commit/db490884fb11b87901824ebd29504991bb6b5bc5))
- **Vue-trello:** rectify mistakce mutation payload for task deletion ([59b1f72](https://github.com/sabertazimi/lab/commit/59b1f72a0ff8ee18caeccba9a88061e94392240c))
- **Vue-trello:** rectify re-navigation route ([a23b89a](https://github.com/sabertazimi/lab/commit/a23b89a3851e085355a836dceecced11e49f1944))
- **Vue-trello:** rectify task drag between columns ([b240f4f](https://github.com/sabertazimi/lab/commit/b240f4fc253c0308871dfe60343d89f4b61fb031))
- **Vue-trello:** refactor to `ColumnTask` component ([9815632](https://github.com/sabertazimi/lab/commit/981563273f588a4b41abc94f701b2802bea709af))
- **Vue-trello:** refactor to more components ([ff7567b](https://github.com/sabertazimi/lab/commit/ff7567b70470ae8af8092b5b17fca265cb8cceca))
- **Vue-vite:** remove @types/react from vite ([#76](https://github.com/sabertazimi/lab/issues/76)) ([c868192](https://github.com/sabertazimi/lab/commit/c868192bc3eea6ad515fbf5b20f70aa8d628f92f)), closes [johnsoncodehk/volar#552](https://github.com/johnsoncodehk/volar/issues/552)
- **Vue-vuex:** change action payload to primitive values ([982c9b5](https://github.com/sabertazimi/lab/commit/982c9b57b6d77419363c93898226e425a03281a1))

# [1.6.0](https://github.com/sabertazimi/lab/compare/v1.5.0...v1.6.0) (2021-09-28)

### Bug Fixes

- **vite-alias:** change `@` to `src` alias path ([96de3ea](https://github.com/sabertazimi/lab/commit/96de3ea94c0fb7fa9afe3e31ba5a9c8f8251ff7d))
- **Vue-button:** add cursor-pointer style to button ([87d0181](https://github.com/sabertazimi/lab/commit/87d0181001339519ae0e5fac7ffab7eff7a5a971))
- **Vue-event:** stop event propagation via `.stop` modifier ([cc539ae](https://github.com/sabertazimi/lab/commit/cc539aec4623e9a1f4fb84a04e69cdb2a28e267f))
- **Vue-router:** `useRouter` for programmatic routes change ([b477bf6](https://github.com/sabertazimi/lab/commit/b477bf67035c3a61ace0de89cee23c5806315adc))
- **Vue-router:** wrap useRoute function ([3b11cd7](https://github.com/sabertazimi/lab/commit/3b11cd733af50e23de689e72dd93a7ad52831ce2))
- **vue-routes:** add nested router view ([e50ff69](https://github.com/sabertazimi/lab/commit/e50ff69757b80ed3c413c1f00131bf0c71d4cb78))
- **Vue-tailwind:** add `.btn` and `.router-link` tailwind components ([d8a9f85](https://github.com/sabertazimi/lab/commit/d8a9f8503cd4bf1f4403df1e7d7f42ad5e0b2ba8))
- **Vue-tailwind:** add `container` and `btn-danger` components ([487315d](https://github.com/sabertazimi/lab/commit/487315d947c5a8157d5c5d0a83baf3823e9d9153))
- **Vue-tailwind:** change text link to button link ([5e9b7dc](https://github.com/sabertazimi/lab/commit/5e9b7dcbabc465780b88e40f26f94c292b084027))
- **Vue-transition:** add list transition ([899a6bc](https://github.com/sabertazimi/lab/commit/899a6bc2d4c84b765cd6633b5cd136147a56719c))
- **Vue-transition:** change fade duration ([2ae054a](https://github.com/sabertazimi/lab/commit/2ae054abe9958e90f6558816103eaaa8adff5474))
- **vue-trello:** add `Board` and `Task` views ([92d2d78](https://github.com/sabertazimi/lab/commit/92d2d7885c561bcca822ed904f6beceaf0493845))
- **Vue-trello:** add `nanoid` package ([187c816](https://github.com/sabertazimi/lab/commit/187c81663b360219f5b73cd65728913458e44e66))
- **Vue-trello:** add close button to `Task` view ([513a403](https://github.com/sabertazimi/lab/commit/513a4037d6b17d75b5d69cac9f2c778ad367d112))
- **Vue-trello:** add columns flex container ([61883c1](https://github.com/sabertazimi/lab/commit/61883c106f63c3048f236b81d58f014f99ad592e))
- **Vue-trello:** add nanoid to column type ([fa94a2b](https://github.com/sabertazimi/lab/commit/fa94a2bceb9ed920278bfe020e2eb247f38750b4))
- **Vue-trello:** add transition for button and input elements ([29b509e](https://github.com/sabertazimi/lab/commit/29b509ebb2a62fdb3de404272094700a2d6ec0de))
- **Vue-trello:** add v3 transition for modal element ([34ba854](https://github.com/sabertazimi/lab/commit/34ba854cdd7f270173636f67b2fd8a02d9d3c725))
- **Vue-trello:** allow task with empty name ([693c87e](https://github.com/sabertazimi/lab/commit/693c87e5dfa6ea9295a0c4eb092eaa0338d31a43))
- **Vue-trello:** change local storage key name for board state ([326f7c5](https://github.com/sabertazimi/lab/commit/326f7c56e2b90ff29738d67eae41a86ceea9ccbf))
- **Vue-trello:** cleanup button tailwind class ([36cc72a](https://github.com/sabertazimi/lab/commit/36cc72a72210667cad0b76bbe965aecae784897c))
- **Vue-trello:** close modal only when empty space clicked ([5804a41](https://github.com/sabertazimi/lab/commit/5804a41d277c38fcf8c8491530797fce0f66976e))
- **Vue-trello:** close modal when empty space clicked ([77090a7](https://github.com/sabertazimi/lab/commit/77090a72d2fa0c4bfd556351d7fcf40676e6eb0e))
- **Vue-trello:** complete update task vuex mutation ([01c5215](https://github.com/sabertazimi/lab/commit/01c5215fa1381e6b74bd94d042e97160c1e49eb0))
- **Vue-trello:** empty input checking ([d1e4ef8](https://github.com/sabertazimi/lab/commit/d1e4ef8e47a11d4b09352c771908d901bef80407))
- **Vue-trello:** implement simple button with tailwind.css ([00caeb2](https://github.com/sabertazimi/lab/commit/00caeb2ed1a9c881a44285a36ef8ef3d7d2a5e98))
- **vue-trello:** load board state from local storage ([ab6d14d](https://github.com/sabertazimi/lab/commit/ab6d14d25d768ecb175d1c4eeec276f3773fd469))
- **Vue-trello:** make close button right alignment ([202ddef](https://github.com/sabertazimi/lab/commit/202ddef95277d6dcb63aea0a0ba4d19ed3ed59db))
- **Vue-trello:** move back home button ([1edf063](https://github.com/sabertazimi/lab/commit/1edf06362243bb7a908fa1293e037ee97301b45c))
- **Vue-trello:** re-position `Task` to `0` px ([e361a3c](https://github.com/sabertazimi/lab/commit/e361a3cfb563f21abad220013777b24a71ca4616))
- **Vue-trello:** remove redundant modal close ([6ce3777](https://github.com/sabertazimi/lab/commit/6ce3777b21f8de102fdbc27b753c60760f579ba9))
- **vue-trello:** setup basic router and state ([f345258](https://github.com/sabertazimi/lab/commit/f3452583b9aaf556665e1593ea6f52dc022cedf3))
- **Vue-trello:** setup basic task columns ([09f75ac](https://github.com/sabertazimi/lab/commit/09f75acf5da929350217dd2c4e154bc16bb96c0b))
- **Vue-trello:** setup tailwind styles for `Board` and `Task` ([adac9f5](https://github.com/sabertazimi/lab/commit/adac9f5d5588dbd15c7740eadfcbf882b2dfdb64))
- **Vue-vite:** access env variables via `import.meta.env` ([fe14d1e](https://github.com/sabertazimi/lab/commit/fe14d1e1c6da740aa6947eceff662ff741ace408))
- **Vue-vite:** change public path for deployment ([770ddcb](https://github.com/sabertazimi/lab/commit/770ddcbad5e2cda3cc4023f442c60a7aea285099))
- **Vue-vuex:** add `createTask` vuex mutation ([b8e4895](https://github.com/sabertazimi/lab/commit/b8e489572ace1a943c92e81cbb6eebde47e63f0b))
- **Vue-vuex:** add delete task vuex mutation ([d4d3718](https://github.com/sabertazimi/lab/commit/d4d3718c630274c931c855fe5908a2c7ee93dd68))
- **Vue-vuex:** add TypeScript types for vuex ([4d2cd90](https://github.com/sabertazimi/lab/commit/4d2cd90f68956101024aad1c40910b24af5665d7))
- **Vue-vuex:** computed value from vuex state ([dab0c7b](https://github.com/sabertazimi/lab/commit/dab0c7be344a0bf6c1c13fb7146924b074d83785))
- **Vue-vuex:** simple vuex plugin to save board state ([ffa6504](https://github.com/sabertazimi/lab/commit/ffa650435bb92217b517bcdbd78a94356fb69ddc))
- **Vue-vuex:** vuex getters ([84a61d4](https://github.com/sabertazimi/lab/commit/84a61d4e4c299a440f1b1e72685456107f2ba9ba))

### Features

- **lint-css:** add `stylelint` support ([902acd0](https://github.com/sabertazimi/lab/commit/902acd0e441e14191fd673093d84087bd3903795))
- **Vue-tailwind:** add tailwind.css support for Vite ([6f4d515](https://github.com/sabertazimi/lab/commit/6f4d51500fcb0c615e05c8b95594239eff5ab5d3))
- **Vue-trello:** start to Vue Trello clone project ([d1da3ed](https://github.com/sabertazimi/lab/commit/d1da3ed21d32e8f37e460d402d9858bd088f6f97))

# [1.5.0](https://github.com/sabertazimi/lab/compare/v1.4.0...v1.5.0) (2021-09-26)

### Bug Fixes

- **API-server:** create mock API with typicode JSON server ([91d2faf](https://github.com/sabertazimi/lab/commit/91d2faf7218ca2ccc6e44467f9c77946df10e0cd))
- **Vue-async:** async `setup` components ([f93912b](https://github.com/sabertazimi/lab/commit/f93912bca3c6762eb9fe1949e61a1f6f8aa3a104))
- **Vue-composition:** Vue 3 composition API with `setup` script ([2af1a57](https://github.com/sabertazimi/lab/commit/2af1a576059e6c5de9948d999d4decea30011575))
- **Vue-learn:** add dynamic router support ([5092014](https://github.com/sabertazimi/lab/commit/5092014d8abf8a646bf27c7e292653779b9d78e8))
- **Vue-learn:** named Vue routes ([60f7887](https://github.com/sabertazimi/lab/commit/60f7887e3a0c07881a2d3764e2fee4cf76a1320b))
- **Vue-learn:** passing route props to component ([0ad19e5](https://github.com/sabertazimi/lab/commit/0ad19e5fd43ad4323dc69d084244c73eb9e0b507))
- **Vue-learn:** remove boilerplate template ([dd4ab07](https://github.com/sabertazimi/lab/commit/dd4ab071712ca93b596f77cae782ebec04e84522))
- **Vue-learn:** remove redundant `v-if` directive ([fd750d5](https://github.com/sabertazimi/lab/commit/fd750d580de7d943274f8c6aca80deffabc574f9))
- **Vue-suspense:** suspense for async components ([5a72970](https://github.com/sabertazimi/lab/commit/5a7297079847eef1f57e0ca8831437adf0fac5d7))

### Features

- **Vue-learn:** cleanup `learn-vue` project ([5aa5642](https://github.com/sabertazimi/lab/commit/5aa5642fd46057bd1bdcc5b25a433d7ebdfc880b))

# [1.4.0](https://github.com/sabertazimi/lab/compare/v1.3.0...v1.4.0) (2021-09-25)

### Bug Fixes

- **deps:** pin dependencies ([#50](https://github.com/sabertazimi/lab/issues/50)) ([c13fc6a](https://github.com/sabertazimi/lab/commit/c13fc6ac7fd68eeaa9a6489958aa4f5073401582))
- **React:** disable production source map generation ([9c3fb73](https://github.com/sabertazimi/lab/commit/9c3fb7357dad649512b488d2198240e8dd9303ec))
- **Vue-CLI:** disable production source maps ([d8fc66c](https://github.com/sabertazimi/lab/commit/d8fc66c7a41304b48275bd4ede8e4e5bad33ced0))
- **Vue:** rectify deployment public path for GitHub Pages ([5db87db](https://github.com/sabertazimi/lab/commit/5db87dbd418a9314fddfc471df346c703972589c))

### Features

- **Vue:** add Vue TypeScript learning demo ([ea93707](https://github.com/sabertazimi/lab/commit/ea93707b2a1d7bddf922799308fbe8dbc2bcb03b))

# [1.3.0](https://github.com/sabertazimi/lab/compare/v1.2.2...v1.3.0) (2021-09-12)

### Features

- **yarn:** switch from npm to yarn berry ([ef61b92](https://github.com/sabertazimi/lab/commit/ef61b928619bdd29c2b92f3ceadf3f72fb6bb5cf))

## [1.2.2](https://github.com/sabertazimi/lab/compare/v1.2.1...v1.2.2) (2021-09-06)

### :rocket: Building Work

- **CI-azure:** remove azure pipelines ([cdcfc00](https://github.com/sabertazimi/lab/commit/cdcfc00e7d5a844900f5775a36fe538f956324cd))
- **CI:** change fetch depth ([a3751d1](https://github.com/sabertazimi/lab/commit/a3751d1c5ec73796fefb8a407a510194e4705536))
- **CI:** separate CI stage ([513e0d1](https://github.com/sabertazimi/lab/commit/513e0d1606a747cc98dc5c625ee0d695a40f6f51))
- **CI:** skip deploy on PRs ([10a72f5](https://github.com/sabertazimi/lab/commit/10a72f5050f00cf3ecca2a95e40b9de893e61fbf))
- **deps-dev:** bump @sabertazimi/react-scripts from 5.0.2 to 5.1.0 ([#35](https://github.com/sabertazimi/lab/issues/35)) ([13c94df](https://github.com/sabertazimi/lab/commit/13c94dfbb909e73afd921ce40188b4efbd1fdbea))
- **deps-dev:** bump @sabertazimi/react-scripts from 5.1.0 to 5.3.3 ([#39](https://github.com/sabertazimi/lab/issues/39)) ([768f2bd](https://github.com/sabertazimi/lab/commit/768f2bd1b485a6acb0bf2cbd5c31b99cc8a57fea))
- **deps-dev:** bump @types/node from 16.7.1 to 16.7.4 ([707db6d](https://github.com/sabertazimi/lab/commit/707db6d868d093b745183a1929bb14fbb852314d))
- **deps-dev:** bump @types/node from 16.7.4 to 16.7.6 ([f828077](https://github.com/sabertazimi/lab/commit/f8280773ff028db4be638139bede2c739795abed))
- **deps-dev:** bump @types/node from 16.7.6 to 16.7.8 ([#34](https://github.com/sabertazimi/lab/issues/34)) ([39ba719](https://github.com/sabertazimi/lab/commit/39ba71916e7d75cc77ede6f2a81b4a6189ca04ca))
- **deps-dev:** bump @types/node from 16.7.8 to 16.7.10 ([#38](https://github.com/sabertazimi/lab/issues/38)) ([fc56d8b](https://github.com/sabertazimi/lab/commit/fc56d8bba94c65e38fd1a4570420e6bf86babfbd))
- **deps-dev:** bump @types/react from 17.0.19 to 17.0.20 ([#37](https://github.com/sabertazimi/lab/issues/37)) ([0a14419](https://github.com/sabertazimi/lab/commit/0a14419d25389a9995c32fd3b4130bd9aca9a362))
- **deps-dev:** bump @typescript-eslint/eslint-plugin ([169df12](https://github.com/sabertazimi/lab/commit/169df12df116832d7d81e781cb97447222359bd1))
- **deps-dev:** bump @typescript-eslint/eslint-plugin ([#32](https://github.com/sabertazimi/lab/issues/32)) ([17949b4](https://github.com/sabertazimi/lab/commit/17949b45c26e68e5d138d48cf6c1f639a3d3198f))
- **deps-dev:** bump @typescript-eslint/parser from 4.29.2 to 4.29.3 ([51302bc](https://github.com/sabertazimi/lab/commit/51302bc2a88a8473ee54c63492bac1e4f3a6d576))
- **deps-dev:** bump @typescript-eslint/parser from 4.29.3 to 4.30.0 ([#36](https://github.com/sabertazimi/lab/issues/36)) ([4750bd5](https://github.com/sabertazimi/lab/commit/4750bd55aca992105d325bd6c3f747ad9b235b25))
- **deps-dev:** bump eslint-plugin-prettier from 3.4.1 to 4.0.0 ([#33](https://github.com/sabertazimi/lab/issues/33)) ([1dba155](https://github.com/sabertazimi/lab/commit/1dba155fd1c61fdb0e790c1271a493ba5677b882))
- **deps-dev:** bump typescript from 4.3.5 to 4.4.2 ([dc2cab7](https://github.com/sabertazimi/lab/commit/dc2cab79b3f2450d303048cf9c4a270c0be47592))

### [1.2.1](https://github.com/sabertazimi/lab/compare/v1.2.0...v1.2.1) (2021-08-27)

### :bug: Bug Fixes

- **deps-ddp:** remove duplicated packages ([b664e51](https://github.com/sabertazimi/lab/commit/b664e515d68353ea9f392228e7e1c7895944f570))
- **Jest-coverage:** disable coverage from `index.tsx` ([5cf28e5](https://github.com/sabertazimi/lab/commit/5cf28e5fd1e31e205237bf4f00b1b356d590aecb))
- **lint:** add explicit stylelint and eslint script ([3ff73fc](https://github.com/sabertazimi/lab/commit/3ff73fc8c43f6ea41c1035adf48cf8dfe65527ee))
- **sandbox-css:** enable postcss normalize ([6b1d430](https://github.com/sabertazimi/lab/commit/6b1d430a301f398b1537a007f4da4cfe0b62eafa))
- **sandbox-css:** rectify css order error ([b484f11](https://github.com/sabertazimi/lab/commit/b484f11bc743b01565fd126d09243eeea4a6a2e9))
- **sandbox-lint:** change lint config to `bod` ([0058a94](https://github.com/sabertazimi/lab/commit/0058a949ed9db730a4976ffc9d0fd1faf36a903b))
- **test:** enable coverage collection ([a55c37f](https://github.com/sabertazimi/lab/commit/a55c37fbca90a18519de1da928cb9ab47cc1e02d))
- **tsconfig:** target to es6 on Node 14 and 16 ([b8609b7](https://github.com/sabertazimi/lab/commit/b8609b7797acf934f7dff4d51ce2ca16d4ce8e75))

### :rocket: Building Work

- **CI-azure:** add more pipeline triggers ([fbcbeff](https://github.com/sabertazimi/lab/commit/fbcbeffc43fa56f829385d9b82ed4f38ac02f88d))
- **CI:** initialize git config ([4993134](https://github.com/sabertazimi/lab/commit/4993134f46658a7a2d30577502f2e14ba935018d))
- **CI:** set up CI with Azure Pipelines ([86e5812](https://github.com/sabertazimi/lab/commit/86e5812965acea6c0df01cf8ccda0b442ba9c611))
- **CI:** setup coveralls action ([ca5bc34](https://github.com/sabertazimi/lab/commit/ca5bc34cf5394c82a86f8f1f12f47ca421a14879))
- **deps-dev:** bump @sabertazimi/react-scripts from 5.0.0 to 5.0.2 ([bdee282](https://github.com/sabertazimi/lab/commit/bdee282cb794bcd6d44408eb11145b20dc257daf))
- **deps-dev:** bump @types/node from 16.6.2 to 16.7.1 ([324bb88](https://github.com/sabertazimi/lab/commit/324bb88276d721ac965fe0938878a4c667979fbd))
- **deps-dev:** bump eslint-plugin-prettier from 3.4.0 to 3.4.1 ([75d2e37](https://github.com/sabertazimi/lab/commit/75d2e37c9d24b3718dfc1baf94361241419a3bbc))
- **deps-dev:** bump pm2 from 5.1.0 to 5.1.1 ([a70d79b](https://github.com/sabertazimi/lab/commit/a70d79bad864d258182d2a4333d770b67cdf79df))
- **deps-dev:** bump ts-node from 10.2.0 to 10.2.1 ([294bd7b](https://github.com/sabertazimi/lab/commit/294bd7b7acc7050fc2821bd18fb54dabbc6d903e))
- **deps:** bump @sabertazimi/react-scripts from 4.0.1 to 5.0.0 ([3071c36](https://github.com/sabertazimi/lab/commit/3071c369bd9915c10ec49c844bf5bf8e007416c4))
- **deps:** bump @types/node from 16.6.1 to 16.6.2 ([6f32f6a](https://github.com/sabertazimi/lab/commit/6f32f6ab75f0e79adb20d25196615cd0209ab5ef))
- **deps:** bump @types/react from 17.0.18 to 17.0.19 ([c0ec093](https://github.com/sabertazimi/lab/commit/c0ec093e644ff1de0b08faaf1c58d6d10e8b5c72))
- **sandbox:** add more react-scripts commands ([dc7175f](https://github.com/sabertazimi/lab/commit/dc7175f371be7a3517744aa7bd0af54152d2acc1))
- **sandbox:** separate deps and devDeps ([37acb6c](https://github.com/sabertazimi/lab/commit/37acb6c4ea7ebf786e861425084cdfa99700533a))

## [1.2.0](https://github.com/sabertazimi/lab/compare/v1.1.3...v1.2.0) (2021-08-17)

### :sparkles: Features

- **bod CLI:** change to @sabertazimi/react-scripts ([9601587](https://github.com/sabertazimi/lab/commit/9601587c800c7003f592f899cb102aaa401459f4))

### [1.1.3](https://github.com/sabertazimi/lab/compare/v1.1.2...v1.1.3) (2021-08-17)

### :rocket: Building Work

- **deps-dev:** bump @typescript-eslint/eslint-plugin ([892cfa4](https://github.com/sabertazimi/lab/commit/892cfa45fe211d7a0ba9a34671cf95361e742916))
- **deps-dev:** bump @typescript-eslint/parser from 4.29.0 to 4.29.1 ([f8f01d5](https://github.com/sabertazimi/lab/commit/f8f01d5b94d636f0d7ad0fcd2d5fe4da7a0b04cd))
- **deps-dev:** bump tslib from 2.3.0 to 2.3.1 ([278afea](https://github.com/sabertazimi/lab/commit/278afeaf4cd7b5d02237be38e9486df80a1ded19))
- **deps:** bump @types/jest from 26.0.24 to 27.0.1 ([3df1369](https://github.com/sabertazimi/lab/commit/3df136947e764b8bbbc21f55ee05ae3568bb93b7))
- **deps:** bump @types/node from 16.4.13 to 16.6.1 ([66e9f3a](https://github.com/sabertazimi/lab/commit/66e9f3ad6643f78e9164a2ec3c3fad4b902ad1c0))
- **deps:** bump @types/react from 17.0.16 to 17.0.18 ([3d0879c](https://github.com/sabertazimi/lab/commit/3d0879cb4ec23ebc0e126e697a5a0f79a5cbc7fc))

### [1.1.2](https://github.com/sabertazimi/lab/compare/v1.1.1...v1.1.2) (2021-08-12)

### :bug: Bug Fixes

- **CI:** rectify build homepage url ([1a6787f](https://github.com/sabertazimi/lab/commit/1a6787f6bd29e6bbf92722453ba51dcc57dc737e))

### :rocket: Building Work

- **deps-dev:** bump ts-node from 10.1.0 to 10.2.0 ([6f0fbc7](https://github.com/sabertazimi/lab/commit/6f0fbc752b49d4b8976e817c7ea20111024e376d))
- **deps:** bump @testing-library/react from 11.2.7 to 12.0.0 ([fa0861b](https://github.com/sabertazimi/lab/commit/fa0861b83c654d9a4d5b4bb321db846034973eba))
- **deps:** bump @testing-library/user-event from 12.8.3 to 13.2.1 ([2bbe144](https://github.com/sabertazimi/lab/commit/2bbe1442b680a3bb69e46207721617a324d7d5a9))
- **deps:** bump @types/node from 16.4.10 to 16.4.13 ([434e2b2](https://github.com/sabertazimi/lab/commit/434e2b26f5a97a77f414e34e075e823ffc67abf0))
- **deps:** bump @types/react from 17.0.15 to 17.0.16 ([d129146](https://github.com/sabertazimi/lab/commit/d1291462fefffa79bbeba5c52e07d76d020ff770))
- **deps:** bump web-vitals from 1.1.2 to 2.1.0 ([7010092](https://github.com/sabertazimi/lab/commit/7010092f4ace1a69373f320c3ee36b50db3bf9c6))
- **React-sandbox:** change sandbox to private package ([d096f6a](https://github.com/sabertazimi/lab/commit/d096f6a34068a699442abe5e4f1198ed0e70a483))

### [1.1.1](https://github.com/sabertazimi/lab/compare/v1.1.0...v1.1.1) (2021-08-03)

### Bug Fixes

- **CI:** rectify CI prefix url ([36185ff](https://github.com/sabertazimi/lab/commit/36185ff5a12b138dad28cd36db4f35ede7ce9b97))
- **release:** move standard-version to root ([50778f0](https://github.com/sabertazimi/lab/commit/50778f0853564077ef1e10b8253789b9fecab7fb))

### Building Work

- **CI:** add more CI scripts ([06b2d01](https://github.com/sabertazimi/lab/commit/06b2d019a420775d1ea0a5ce4901c33affd8fb49))
- **deps-dev:** bump @typescript-eslint/eslint-plugin from 4.28.5 to 4.29.0 ([d9ce4ce](https://github.com/sabertazimi/lab/commit/d9ce4ce55b098635338089770bb22f656e998c4c))
- **deps-dev:** bump @typescript-eslint/parser from 4.28.5 to 4.29.0 ([81c1265](https://github.com/sabertazimi/lab/commit/81c12654a5ab60f15f2c510c7af16813aaaf8bbf))
- **release:** add standard-version support for workspaces ([957ab63](https://github.com/sabertazimi/lab/commit/957ab63f5b8f9998a9bcf2066d85f7eca39221dd))

## [1.1.0](https://github.com/sabertazimi/lab/compare/v1.0.2...v1.1.0) (2021-08-03)

### Features

- **React-sandbox:** add React sandbox project ([2ed317a](https://github.com/sabertazimi/lab/commit/2ed317a68e8bd83032caacd5a61d560b138cdcf3)), closes [#2](https://github.com/sabertazimi/lab/issues/2)
- **workspaces:** add NPM workspaces support ([f23f59b](https://github.com/sabertazimi/lab/commit/f23f59baca0f214ac068181f5b9672d09cdabdfc)), closes [#2](https://github.com/sabertazimi/lab/issues/2)

### Building Work

- **CI:** remove setup.sh bash script ([13f4224](https://github.com/sabertazimi/lab/commit/13f4224826cf58c4ee5653c396d9e4d46cb1faca)), closes [#2](https://github.com/sabertazimi/lab/issues/2)
- **deps-dev:** bump @types/node from 16.4.3 to 16.4.10 ([4673894](https://github.com/sabertazimi/lab/commit/467389489e731cd3b95966b17efb1f6d0e476b7c))
- **deps-dev:** bump eslint from 7.31.0 to 7.32.0 ([3c9eaef](https://github.com/sabertazimi/lab/commit/3c9eaef0c947bac1bdeeb0b18b1470bc317c4a4b))

### [1.0.2](https://github.com/sabertazimi/lab/compare/v1.0.1...v1.0.2) (2021-08-02)

### Bug Fixes

- **release:** tag with signature ([cdfdac0](https://github.com/sabertazimi/lab/commit/cdfdac0446ba60a60f765a3f4cf2eabe60090ea8))

### [1.0.1](https://github.com/sabertazimi/lab/compare/v1.0.0...v1.0.1) (2021-08-02)

### Building Work

- **CHANGELOG:** add more fields to CHANGELOG ([bc85c41](https://github.com/sabertazimi/lab/commit/bc85c41256e122324322b1d6bd61c908353d067f))

## 1.0.0 (2021-08-01)

### Features

- **release:** add standard-version support ([9ca6684](https://github.com/sabertazimi/lab/commit/9ca6684a10688578625f143395715cfd001d4588))
