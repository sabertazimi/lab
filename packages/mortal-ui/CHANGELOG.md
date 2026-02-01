# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.2.0](https://github.com/sabertazimi/lab/compare/v3.1.0...v3.2.0) (2026-02-01)

**Note:** Version bump only for package @lab/mortal-ui

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

**Note:** Version bump only for package @lab/mortal-ui

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

**Note:** Version bump only for package mortal-ui

# [2.2.0](https://github.com/sabertazimi/lab/compare/v2.1.0...v2.2.0) (2025-12-12)

**Note:** Version bump only for package mortal-ui

# [2.1.0](https://github.com/sabertazimi/lab/compare/v2.0.0...v2.1.0) (2025-12-10)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#870](https://github.com/sabertazimi/lab/issues/870)) ([f3d83b1](https://github.com/sabertazimi/lab/commit/f3d83b1804abe28ce0053a20df8111ccdd9be45b))

# [2.0.0](https://github.com/sabertazimi/lab/compare/v1.10.0...v2.0.0) (2025-12-04)

**Note:** Version bump only for package mortal-ui

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
- **deps:** update dependency element-plus to ^2.10.1 ([#781](https://github.com/sabertazimi/lab/issues/781)) ([ea91ebf](https://github.com/sabertazimi/lab/commit/ea91ebfe98b75ab5f9d139505ddc76e87eef6114))
- **deps:** update dependency element-plus to ^2.11.1 ([#822](https://github.com/sabertazimi/lab/issues/822)) ([6bd2738](https://github.com/sabertazimi/lab/commit/6bd2738e069e99ce045013ec1f8d469648b55685))
- **deps:** update dependency element-plus to ^2.7.1 ([#638](https://github.com/sabertazimi/lab/issues/638)) ([b0587bc](https://github.com/sabertazimi/lab/commit/b0587bcbc2db1b2ace57ff02e6e2f44c43772e76))
- **deps:** update dependency element-plus to ^2.9.9 ([#773](https://github.com/sabertazimi/lab/issues/773)) ([7beaceb](https://github.com/sabertazimi/lab/commit/7beaceb4870b76b47e3a627ff71b3a5e35319494))
- **deps:** update dependency pinia to v3 ([#747](https://github.com/sabertazimi/lab/issues/747)) ([cb593bc](https://github.com/sabertazimi/lab/commit/cb593bc766c0ad17f01a731b32366778c4e9a38a))
- **deps:** update dependency vue to ^3.5.11 ([#702](https://github.com/sabertazimi/lab/issues/702)) ([aecee85](https://github.com/sabertazimi/lab/commit/aecee85c8ee658d99054118afd77f179618d3547))
- **deps:** update dependency vue-i18n to ^10.0.2 ([#698](https://github.com/sabertazimi/lab/issues/698)) ([9e44560](https://github.com/sabertazimi/lab/commit/9e445601733da0feb0a2cdd3ac48fa62c248d84c))
- **deps:** update dependency vue-i18n to ^10.0.3 ([#700](https://github.com/sabertazimi/lab/issues/700)) ([fa4d25d](https://github.com/sabertazimi/lab/commit/fa4d25d759011528349403e6a95212914dd07726))
- **deps:** update dependency vue-i18n to ^10.0.4 ([#703](https://github.com/sabertazimi/lab/issues/703)) ([ed3bdea](https://github.com/sabertazimi/lab/commit/ed3bdea8425ba5082c5a2f1612725f2b7c69f3eb))
- **deps:** update dependency vue-i18n to ^11.1.3 ([#767](https://github.com/sabertazimi/lab/issues/767)) ([02cc678](https://github.com/sabertazimi/lab/commit/02cc6780e5999f76c42c20f917aed7701e712915))
- **deps:** update dependency vue-i18n to ^11.1.7 ([#785](https://github.com/sabertazimi/lab/issues/785)) ([ed9e5fe](https://github.com/sabertazimi/lab/commit/ed9e5fed4225645ac83c025ac0bedc808893307d))
- **deps:** update dependency vue-i18n to ^9.12.1 ([#634](https://github.com/sabertazimi/lab/issues/634)) ([ced9988](https://github.com/sabertazimi/lab/commit/ced99884cbefcd55fefe66804b315ff6740d3a51))
- **deps:** update dependency vue-i18n to ^9.13.1 ([#640](https://github.com/sabertazimi/lab/issues/640)) ([7f5942f](https://github.com/sabertazimi/lab/commit/7f5942fdb3023ad2ea21d04e64470e28e55cb966))
- **deps:** update dependency vue-i18n to v10 ([#692](https://github.com/sabertazimi/lab/issues/692)) ([faabf20](https://github.com/sabertazimi/lab/commit/faabf2057e8b886c6f5eaa988286f1c8b2319f57))
- **deps:** update dependency vue-i18n to v11 ([#726](https://github.com/sabertazimi/lab/issues/726)) ([90f60f8](https://github.com/sabertazimi/lab/commit/90f60f8534a10681553f11486854a8c7d7c2c2c2))

### Features

- **react-shadcn/ui:** add M.League reviewer app ([#850](https://github.com/sabertazimi/lab/issues/850)) ([b3b7e9b](https://github.com/sabertazimi/lab/commit/b3b7e9b4f83f241dfaadfe6c1d6dd00a92bbd680))

### Performance Improvements

- [ImgBot] optimize images ([#851](https://github.com/sabertazimi/lab/issues/851)) ([4a83e07](https://github.com/sabertazimi/lab/commit/4a83e07826fc867e9c90a8f82d9062de8d9198a2))

# [1.9.0](https://github.com/sabertazimi/lab/compare/v1.8.0...v1.9.0) (2024-04-01)

### Bug Fixes

- add logic for dahai after claim ([#606](https://github.com/sabertazimi/lab/issues/606)) ([58eb700](https://github.com/sabertazimi/lab/commit/58eb700ba70135abe5dd976d1bd6723e7a1a325a))
- **deps:** update dependency @unhead/vue to ^1.8.20 ([#610](https://github.com/sabertazimi/lab/issues/610)) ([9406d0d](https://github.com/sabertazimi/lab/commit/9406d0d47a6159bc82ad475b4dbdcdd0d7db8300))
- **deps:** update dependency @unhead/vue to ^1.9.4 ([#619](https://github.com/sabertazimi/lab/issues/619)) ([8084314](https://github.com/sabertazimi/lab/commit/8084314c9cdae592c56927c56b197d8f84bdf94c))
- **mortal:** rectify build prefix path bug ([#604](https://github.com/sabertazimi/lab/issues/604)) ([89287be](https://github.com/sabertazimi/lab/commit/89287bede4bff1ad0163c2608721f567adcdd27b))

### Features

- **mortal:** add Mortal GUI Vue project ([#602](https://github.com/sabertazimi/lab/issues/602)) ([62baa1e](https://github.com/sabertazimi/lab/commit/62baa1edea6eca0ab331cf9c221953824854199a))
- show expected and actual choices ([#605](https://github.com/sabertazimi/lab/issues/605)) ([d56c994](https://github.com/sabertazimi/lab/commit/d56c9941d919270c337a1623348350dd09348b71))
