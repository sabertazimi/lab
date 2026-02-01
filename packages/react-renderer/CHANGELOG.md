# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.2.0](https://github.com/sabertazimi/lab/compare/v3.1.0...v3.2.0) (2026-02-01)

**Note:** Version bump only for package @lab/react-renderer

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

**Note:** Version bump only for package @lab/react-renderer

# [3.0.0](https://github.com/sabertazimi/lab/compare/v2.5.0...v3.0.0) (2026-01-28)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#929](https://github.com/sabertazimi/lab/issues/929)) ([645c3dc](https://github.com/sabertazimi/lab/commit/645c3dcbfd7315294fdde7778c47f4b6aae545ba))
- **deps:** update dependencies (non-major) ([#933](https://github.com/sabertazimi/lab/issues/933)) ([465b4e4](https://github.com/sabertazimi/lab/commit/465b4e407553663fc9d8359950fef8f56459e18e))

- feat(rust)!: add rust learning workspace with rustlings, exercism, and docs (#935) ([cfa6854](https://github.com/sabertazimi/lab/commit/cfa6854932c3bf4476e99c39403c621320f89916)), closes [#935](https://github.com/sabertazimi/lab/issues/935)

### Features

- **dblp:** add DBLP search application ([#936](https://github.com/sabertazimi/lab/issues/936)) ([1faf657](https://github.com/sabertazimi/lab/commit/1faf657f95c5ed766ee0d82caa7baa1b1ef0845f))

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

- **react-renderer:** update favicon reference to `logo.svg` ([1033374](https://github.com/sabertazimi/lab/commit/103337424efbc7bdc3585a81d8d2b9be535e7d57))

### Features

- **build:** add Vercel deployment support with centralized post-buil… ([#921](https://github.com/sabertazimi/lab/issues/921)) ([1a2bbe5](https://github.com/sabertazimi/lab/commit/1a2bbe5dfbe0c36d18ad2c2d24343a332fe5e61f))

# [2.4.0](https://github.com/sabertazimi/lab/compare/v2.3.0...v2.4.0) (2025-12-21)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#914](https://github.com/sabertazimi/lab/issues/914)) ([5cf2bd4](https://github.com/sabertazimi/lab/commit/5cf2bd48ed243f1e590a320bd8af730bebe629ed))

# [2.3.0](https://github.com/sabertazimi/lab/compare/v2.2.0...v2.3.0) (2025-12-15)

**Note:** Version bump only for package @lab/react-renderer

# [2.2.0](https://github.com/sabertazimi/lab/compare/v2.1.0...v2.2.0) (2025-12-12)

**Note:** Version bump only for package @lab/react-renderer

# [2.1.0](https://github.com/sabertazimi/lab/compare/v2.0.0...v2.1.0) (2025-12-10)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#870](https://github.com/sabertazimi/lab/issues/870)) ([f3d83b1](https://github.com/sabertazimi/lab/commit/f3d83b1804abe28ce0053a20df8111ccdd9be45b))

# [2.0.0](https://github.com/sabertazimi/lab/compare/v1.10.0...v2.0.0) (2025-12-04)

### Features

- **portfolio:** implement projects portfolio grid ([#867](https://github.com/sabertazimi/lab/issues/867)) ([434ce64](https://github.com/sabertazimi/lab/commit/434ce6410529fda51909803fcd5bb090118b3d75))

# [1.10.0](https://github.com/sabertazimi/lab/compare/v1.9.0...v1.10.0) (2025-12-03)

### Bug Fixes

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
- **deps:** update dependencies (non-major) ([#853](https://github.com/sabertazimi/lab/issues/853)) ([0e1acdf](https://github.com/sabertazimi/lab/commit/0e1acdf03aa3fbca19b0057366ed414a75607226))
- **deps:** update dependency @types/node to ^22.15.34 ([#790](https://github.com/sabertazimi/lab/issues/790)) ([ec882fd](https://github.com/sabertazimi/lab/commit/ec882fd11c9ac4bfc05505b2e155e2deac882d9b))
- **deps:** update dependency @types/node to ^22.16.5 ([#800](https://github.com/sabertazimi/lab/issues/800)) ([fc43b73](https://github.com/sabertazimi/lab/commit/fc43b738c10e0b205a4f4bf56929da099516a58e))
- **deps:** update dependency @types/node to v24 ([#845](https://github.com/sabertazimi/lab/issues/845)) ([06f48e3](https://github.com/sabertazimi/lab/commit/06f48e3cd5b3bcea0fdb07cca1c03dcab37f900b))
- **deps:** update dependency web-vitals to v4 ([#649](https://github.com/sabertazimi/lab/issues/649)) ([28257ea](https://github.com/sabertazimi/lab/commit/28257ead46e445caa9a90b7867e77a0ef29b44e1))
- **react:** remove unused web-vitals package ([#650](https://github.com/sabertazimi/lab/issues/650)) ([cdc60a2](https://github.com/sabertazimi/lab/commit/cdc60a282c6b850ff392b27aabc29b3c418d953d))

### Features

- **react-shadcn/ui:** add M.League reviewer app ([#850](https://github.com/sabertazimi/lab/issues/850)) ([b3b7e9b](https://github.com/sabertazimi/lab/commit/b3b7e9b4f83f241dfaadfe6c1d6dd00a92bbd680))
- **vue-echarts:** echarts dashboard ([#777](https://github.com/sabertazimi/lab/issues/777)) ([8c602d8](https://github.com/sabertazimi/lab/commit/8c602d80571fbd701c23957c2357ce50863a1507))

# [1.9.0](https://github.com/sabertazimi/lab/compare/v1.8.0...v1.9.0) (2024-04-01)

**Note:** Version bump only for package @lab/react-renderer

# [1.8.0](https://github.com/sabertazimi/lab/compare/v1.7.1...v1.8.0) (2022-08-29)

### Bug Fixes

- **deps:** update dependency web-vitals to v3 ([#376](https://github.com/sabertazimi/lab/issues/376)) ([b3dd57f](https://github.com/sabertazimi/lab/commit/b3dd57f8259cdb1d42a51c0f9d33d62dd4fb6d0c))

## [1.7.1](https://github.com/sabertazimi/lab/compare/v1.7.0...v1.7.1) (2022-05-27)

### Bug Fixes

- **deps:** update react monorepo to v18 ([#306](https://github.com/sabertazimi/lab/issues/306)) ([035a11d](https://github.com/sabertazimi/lab/commit/035a11d4730874e23463a8b01a79f94128ed3ae0))
- **react-renderer:** implement React 18 style renderer ([#302](https://github.com/sabertazimi/lab/issues/302)) ([4b3f8a6](https://github.com/sabertazimi/lab/commit/4b3f8a6af95096df782b08569c898a741cf3da98))

# [1.7.0](https://github.com/sabertazimi/lab/compare/v1.6.1...v1.7.0) (2022-03-24)

### Bug Fixes

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

### Features

- **react-renderer:** setup custom React renderer ([#295](https://github.com/sabertazimi/lab/issues/295)) ([953c221](https://github.com/sabertazimi/lab/commit/953c221b5171a65605d073e28be59924705260a5))

## [1.6.1](https://github.com/sabertazimi/lab/compare/v1.6.0...v1.6.1) (2021-10-04)

**Note:** Version bump only for package @lab/react-renderer

# [1.6.0](https://github.com/sabertazimi/lab/compare/v1.5.0...v1.6.0) (2021-09-28)

**Note:** Version bump only for package @lab/react-renderer

# [1.5.0](https://github.com/sabertazimi/lab/compare/v1.4.0...v1.5.0) (2021-09-26)

**Note:** Version bump only for package @lab/react-renderer

# [1.4.0](https://github.com/sabertazimi/lab/compare/v1.3.0...v1.4.0) (2021-09-25)

### Bug Fixes

- **deps:** pin dependencies ([#50](https://github.com/sabertazimi/lab/issues/50)) ([c13fc6a](https://github.com/sabertazimi/lab/commit/c13fc6ac7fd68eeaa9a6489958aa4f5073401582))
- **React:** disable production source map generation ([9c3fb73](https://github.com/sabertazimi/lab/commit/9c3fb7357dad649512b488d2198240e8dd9303ec))

# [1.3.0](https://github.com/sabertazimi/lab/compare/v1.2.2...v1.3.0) (2021-09-12)

### Features

- **yarn:** switch from npm to yarn berry ([ef61b92](https://github.com/sabertazimi/lab/commit/ef61b928619bdd29c2b92f3ceadf3f72fb6bb5cf))
