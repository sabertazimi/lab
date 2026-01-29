# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

**Note:** Version bump only for package @lab/vue-trello

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

**Note:** Version bump only for package @lab/vue-trello

# [2.2.0](https://github.com/sabertazimi/lab/compare/v2.1.0...v2.2.0) (2025-12-12)

**Note:** Version bump only for package @lab/vue-trello

# [2.1.0](https://github.com/sabertazimi/lab/compare/v2.0.0...v2.1.0) (2025-12-10)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#870](https://github.com/sabertazimi/lab/issues/870)) ([f3d83b1](https://github.com/sabertazimi/lab/commit/f3d83b1804abe28ce0053a20df8111ccdd9be45b))

# [2.0.0](https://github.com/sabertazimi/lab/compare/v1.10.0...v2.0.0) (2025-12-04)

**Note:** Version bump only for package @lab/vue-trello

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
- **deps:** update dependency nanoid to ^5.1.2 ([#752](https://github.com/sabertazimi/lab/issues/752)) ([89e2812](https://github.com/sabertazimi/lab/commit/89e281206ef89383c3472bbc2ac6d5d8a1462129))
- **deps:** update dependency nanoid to ^5.1.4 ([#761](https://github.com/sabertazimi/lab/issues/761)) ([1aff3b4](https://github.com/sabertazimi/lab/commit/1aff3b4ef517e6ff39983874f34a551ae419008e))
- **deps:** update dependency vue to ^3.5.11 ([#702](https://github.com/sabertazimi/lab/issues/702)) ([aecee85](https://github.com/sabertazimi/lab/commit/aecee85c8ee658d99054118afd77f179618d3547))

### Features

- **react-shadcn/ui:** add M.League reviewer app ([#850](https://github.com/sabertazimi/lab/issues/850)) ([b3b7e9b](https://github.com/sabertazimi/lab/commit/b3b7e9b4f83f241dfaadfe6c1d6dd00a92bbd680))

# [1.9.0](https://github.com/sabertazimi/lab/compare/v1.8.0...v1.9.0) (2024-04-01)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#504](https://github.com/sabertazimi/lab/issues/504)) ([86827fb](https://github.com/sabertazimi/lab/commit/86827fbdec15bac30b8270d553a286bc5fe09bb5))
- **deps:** update dependency nanoid to ^4.0.1 ([#445](https://github.com/sabertazimi/lab/issues/445)) ([97b3884](https://github.com/sabertazimi/lab/commit/97b38840315185aa94b5e71f421e203c9a560573))
- **deps:** update dependency nanoid to ^4.0.2 ([#473](https://github.com/sabertazimi/lab/issues/473)) ([17e6ee5](https://github.com/sabertazimi/lab/commit/17e6ee51b184d1f6cf42550ae456a75a1b8876e2))
- **deps:** update dependency nanoid to v5 ([#526](https://github.com/sabertazimi/lab/issues/526)) ([43b8887](https://github.com/sabertazimi/lab/commit/43b888738e4f7baf1e937bd61dbd8e766f93102e))
- switch to eslint flat config ([#607](https://github.com/sabertazimi/lab/issues/607)) ([7fecdae](https://github.com/sabertazimi/lab/commit/7fecdae1f27a4c636943b87eb2f2efa0ae192213))

# [1.8.0](https://github.com/sabertazimi/lab/compare/v1.7.1...v1.8.0) (2022-08-29)

### Bug Fixes

- **deps:** update dependency nanoid to v4 ([#347](https://github.com/sabertazimi/lab/issues/347)) ([9260f1f](https://github.com/sabertazimi/lab/commit/9260f1fd76825fb577e25593a632ef93c85fe6cc))

## [1.7.1](https://github.com/sabertazimi/lab/compare/v1.7.0...v1.7.1) (2022-05-27)

**Note:** Version bump only for package @lab/vue-trello

# [1.7.0](https://github.com/sabertazimi/lab/compare/v1.6.1...v1.7.0) (2022-03-24)

### Bug Fixes

- **deps:** update dependency nanoid to ^3.1.29 ([#85](https://github.com/sabertazimi/lab/issues/85)) ([7bb1a51](https://github.com/sabertazimi/lab/commit/7bb1a513bfd8de7ad93f64bc1f0695a36b6c58ad))
- **deps:** update dependency nanoid to ^3.1.30 ([#106](https://github.com/sabertazimi/lab/issues/106)) ([6223621](https://github.com/sabertazimi/lab/commit/6223621d796e20d623073422a09944914761973f))
- **deps:** update dependency nanoid to ^3.2.0 ([#238](https://github.com/sabertazimi/lab/issues/238)) ([82e46c5](https://github.com/sabertazimi/lab/commit/82e46c52cd61f8fef09cc00702ecf8efb2717726))
- **deps:** update dependency nanoid to ^3.3.1 ([#259](https://github.com/sabertazimi/lab/issues/259)) ([378f02d](https://github.com/sabertazimi/lab/commit/378f02db78f04bc74f82add875304742495c728e))
- **deps:** update dependency vue-router to ^4.0.13 ([#276](https://github.com/sabertazimi/lab/issues/276)) ([b1c285d](https://github.com/sabertazimi/lab/commit/b1c285d93ee0155f1e77421dd783e5981c564e00))
- **deps:** update dependency vue-router to ^4.0.14 ([#286](https://github.com/sabertazimi/lab/issues/286)) ([87b62d4](https://github.com/sabertazimi/lab/commit/87b62d499018c7d6e4901271866039739ecd16f7))

## [1.6.1](https://github.com/sabertazimi/lab/compare/v1.6.0...v1.6.1) (2021-10-04)

### Bug Fixes

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
