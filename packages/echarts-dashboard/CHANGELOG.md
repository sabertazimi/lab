# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

**Note:** Version bump only for package @lab/echarts-dashboard

# [3.0.0](https://github.com/sabertazimi/lab/compare/v2.5.0...v3.0.0) (2026-01-28)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#929](https://github.com/sabertazimi/lab/issues/929)) ([645c3dc](https://github.com/sabertazimi/lab/commit/645c3dcbfd7315294fdde7778c47f4b6aae545ba))

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

### Features

- **build:** add Vercel deployment support with centralized post-buil… ([#921](https://github.com/sabertazimi/lab/issues/921)) ([1a2bbe5](https://github.com/sabertazimi/lab/commit/1a2bbe5dfbe0c36d18ad2c2d24343a332fe5e61f))

# [2.4.0](https://github.com/sabertazimi/lab/compare/v2.3.0...v2.4.0) (2025-12-21)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#914](https://github.com/sabertazimi/lab/issues/914)) ([5cf2bd4](https://github.com/sabertazimi/lab/commit/5cf2bd48ed243f1e590a320bd8af730bebe629ed))

# [2.3.0](https://github.com/sabertazimi/lab/compare/v2.2.0...v2.3.0) (2025-12-15)

**Note:** Version bump only for package echarts-dashboard

# [2.2.0](https://github.com/sabertazimi/lab/compare/v2.1.0...v2.2.0) (2025-12-12)

**Note:** Version bump only for package echarts-dashboard

# [2.1.0](https://github.com/sabertazimi/lab/compare/v2.0.0...v2.1.0) (2025-12-10)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#870](https://github.com/sabertazimi/lab/issues/870)) ([f3d83b1](https://github.com/sabertazimi/lab/commit/f3d83b1804abe28ce0053a20df8111ccdd9be45b))

### Performance Improvements

- [ImgBot] optimize images ([#868](https://github.com/sabertazimi/lab/issues/868)) ([c5cd126](https://github.com/sabertazimi/lab/commit/c5cd126855ed1760ba0af55d0d66a3eb493e64a2))

# [2.0.0](https://github.com/sabertazimi/lab/compare/v1.10.0...v2.0.0) (2025-12-04)

**Note:** Version bump only for package echarts-dashboard

# [1.10.0](https://github.com/sabertazimi/lab/compare/v1.9.0...v1.10.0) (2025-12-03)

### Bug Fixes

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
- **deps:** update dependency @vueuse/core to v14 ([#844](https://github.com/sabertazimi/lab/issues/844)) ([8c268cb](https://github.com/sabertazimi/lab/commit/8c268cb193cc1839b581ae1115a5f683f581f425))
- **deps:** update dependency echarts to v6 ([#810](https://github.com/sabertazimi/lab/issues/810)) ([bf2da80](https://github.com/sabertazimi/lab/commit/bf2da807e232af3f9ad17fa2ba91f25d47d1252e))
- **deps:** update dependency vue-echarts to v7 ([#779](https://github.com/sabertazimi/lab/issues/779)) ([200fa72](https://github.com/sabertazimi/lab/commit/200fa723a2db68caa3e3571829136d5bb9f7db77))
- **deps:** update dependency vue-echarts to v8 ([#831](https://github.com/sabertazimi/lab/issues/831)) ([841190b](https://github.com/sabertazimi/lab/commit/841190b5c4f1b4c34ffe9d222a7fc514db5709b9))
- **vue-echarts:** add scatter symbol ([427eef8](https://github.com/sabertazimi/lab/commit/427eef859946876cb863e30052289edc7a0f7483))
- **vue-echarts:** rectify base url ([b3a416c](https://github.com/sabertazimi/lab/commit/b3a416c03ccad1e022584ed26210c3b8ac03f212))

### Features

- **m.league-design:** change to void zero style ([#858](https://github.com/sabertazimi/lab/issues/858)) ([4783b86](https://github.com/sabertazimi/lab/commit/4783b86fac3948cee38af0ba0384a6f88457cc1d))
- **react-shadcn/ui:** add M.League reviewer app ([#850](https://github.com/sabertazimi/lab/issues/850)) ([b3b7e9b](https://github.com/sabertazimi/lab/commit/b3b7e9b4f83f241dfaadfe6c1d6dd00a92bbd680))
- **vue-echarts:** echarts dashboard ([#777](https://github.com/sabertazimi/lab/issues/777)) ([8c602d8](https://github.com/sabertazimi/lab/commit/8c602d80571fbd701c23957c2357ce50863a1507))

### Performance Improvements

- [ImgBot] optimize images ([#851](https://github.com/sabertazimi/lab/issues/851)) ([4a83e07](https://github.com/sabertazimi/lab/commit/4a83e07826fc867e9c90a8f82d9062de8d9198a2))
