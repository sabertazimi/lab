# Change Log

All notable changes to this project will be documented in this file.
See [Conventional Commits](https://conventionalcommits.org) for commit guidelines.

# [3.2.0](https://github.com/sabertazimi/lab/compare/v3.1.0...v3.2.0) (2026-02-01)

**Note:** Version bump only for package @lab/vue-design

# [3.1.0](https://github.com/sabertazimi/lab/compare/v3.0.0...v3.1.0) (2026-01-29)

**Note:** Version bump only for package @lab/vue-design

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

**Note:** Version bump only for package @lab/vue-design

# [2.2.0](https://github.com/sabertazimi/lab/compare/v2.1.0...v2.2.0) (2025-12-12)

**Note:** Version bump only for package @lab/vue-design

# [2.1.0](https://github.com/sabertazimi/lab/compare/v2.0.0...v2.1.0) (2025-12-10)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#870](https://github.com/sabertazimi/lab/issues/870)) ([f3d83b1](https://github.com/sabertazimi/lab/commit/f3d83b1804abe28ce0053a20df8111ccdd9be45b))

# [2.0.0](https://github.com/sabertazimi/lab/compare/v1.10.0...v2.0.0) (2025-12-04)

### Features

- **portfolio:** implement projects portfolio grid ([#867](https://github.com/sabertazimi/lab/issues/867)) ([434ce64](https://github.com/sabertazimi/lab/commit/434ce6410529fda51909803fcd5bb090118b3d75))

# [1.10.0](https://github.com/sabertazimi/lab/compare/v1.9.0...v1.10.0) (2025-12-03)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#714](https://github.com/sabertazimi/lab/issues/714)) ([25ec0e0](https://github.com/sabertazimi/lab/commit/25ec0e074e2a7491560e4d3245d5da30ad77ca99))
- **deps:** update dependencies (non-major) ([#728](https://github.com/sabertazimi/lab/issues/728)) ([9d7e790](https://github.com/sabertazimi/lab/commit/9d7e790a58a35c8c89e16cd0c0d58163ce3e07fc))
- **deps:** update dependencies (non-major) ([#729](https://github.com/sabertazimi/lab/issues/729)) ([decb678](https://github.com/sabertazimi/lab/commit/decb67840784bbbf3e9eb284b4aa7e1e18079d18))
- **deps:** update dependencies (non-major) ([#738](https://github.com/sabertazimi/lab/issues/738)) ([f65ce87](https://github.com/sabertazimi/lab/commit/f65ce872656215a4a4a583653f3882f29074d1dd))
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
- **deps:** update dependencies (non-major) ([#782](https://github.com/sabertazimi/lab/issues/782)) ([b178f67](https://github.com/sabertazimi/lab/commit/b178f6719164335ab9405a843dfea0f922746439))
- **deps:** update dependencies (non-major) ([#786](https://github.com/sabertazimi/lab/issues/786)) ([1468ebf](https://github.com/sabertazimi/lab/commit/1468ebf575044c5b67eedc78694cf22355307581))
- **deps:** update dependencies (non-major) ([#792](https://github.com/sabertazimi/lab/issues/792)) ([6a49068](https://github.com/sabertazimi/lab/commit/6a490686fc20393f04804d4490ff4a4d7292c0e1))
- **deps:** update dependencies (non-major) ([#796](https://github.com/sabertazimi/lab/issues/796)) ([df4f761](https://github.com/sabertazimi/lab/commit/df4f761271296377c6486de0baa7f59443d5fccf))
- **deps:** update dependencies (non-major) ([#797](https://github.com/sabertazimi/lab/issues/797)) ([39136ea](https://github.com/sabertazimi/lab/commit/39136ea6adc7647c66b1eb55015d885b0b944106))
- **deps:** update dependencies (non-major) ([#802](https://github.com/sabertazimi/lab/issues/802)) ([4935731](https://github.com/sabertazimi/lab/commit/49357312783bd56e66357ac34175847282802450))
- **deps:** update dependencies (non-major) ([#807](https://github.com/sabertazimi/lab/issues/807)) ([41affc2](https://github.com/sabertazimi/lab/commit/41affc2ddff3828d6c4174ed6b4ff319a1f2757e))
- **deps:** update dependencies (non-major) ([#811](https://github.com/sabertazimi/lab/issues/811)) ([84ed9f6](https://github.com/sabertazimi/lab/commit/84ed9f66bf3f7c3b35dbbfa3f65efadb2d57b88f))
- **deps:** update dependencies (non-major) ([#819](https://github.com/sabertazimi/lab/issues/819)) ([3f238df](https://github.com/sabertazimi/lab/commit/3f238dfe82f0f9211aa78612a4db606d0923da43))
- **deps:** update dependencies (non-major) ([#821](https://github.com/sabertazimi/lab/issues/821)) ([733e40d](https://github.com/sabertazimi/lab/commit/733e40dec33f37d446d7b15a677541fd71196d81))
- **deps:** update dependencies (non-major) ([#824](https://github.com/sabertazimi/lab/issues/824)) ([9caa4d8](https://github.com/sabertazimi/lab/commit/9caa4d8d22c3a3e346fe18eba6d31b323ad1c896))
- **deps:** update dependencies (non-major) ([#827](https://github.com/sabertazimi/lab/issues/827)) ([f7f4ec5](https://github.com/sabertazimi/lab/commit/f7f4ec5c25769f2113c453b4b64ef824bd3d01fe))
- **deps:** update dependencies (non-major) ([#829](https://github.com/sabertazimi/lab/issues/829)) ([8239258](https://github.com/sabertazimi/lab/commit/8239258951f4fe58bbac9a28c9a4e36286861607))
- **deps:** update dependencies (non-major) ([#833](https://github.com/sabertazimi/lab/issues/833)) ([59a0ace](https://github.com/sabertazimi/lab/commit/59a0ace102d892db917d07eb023f30d631ad30ec))
- **deps:** update dependencies (non-major) ([#839](https://github.com/sabertazimi/lab/issues/839)) ([6d5d0bc](https://github.com/sabertazimi/lab/commit/6d5d0bc5394b968aeb18af870cc0a76e59f8206c))
- **deps:** update dependencies (non-major) ([#853](https://github.com/sabertazimi/lab/issues/853)) ([0e1acdf](https://github.com/sabertazimi/lab/commit/0e1acdf03aa3fbca19b0057366ed414a75607226))

### Features

- **react-shadcn/ui:** add M.League reviewer app ([#850](https://github.com/sabertazimi/lab/issues/850)) ([b3b7e9b](https://github.com/sabertazimi/lab/commit/b3b7e9b4f83f241dfaadfe6c1d6dd00a92bbd680))

# [1.9.0](https://github.com/sabertazimi/lab/compare/v1.8.0...v1.9.0) (2024-04-01)

### Bug Fixes

- **deps:** update dependencies (non-major) ([#504](https://github.com/sabertazimi/lab/issues/504)) ([86827fb](https://github.com/sabertazimi/lab/commit/86827fbdec15bac30b8270d553a286bc5fe09bb5))
- **deps:** update dependency snabbdom to ^3.6.0 ([#583](https://github.com/sabertazimi/lab/issues/583)) ([dffcf3a](https://github.com/sabertazimi/lab/commit/dffcf3ab630bce82518df54b76dc933066d0210c))
- switch to eslint flat config ([#607](https://github.com/sabertazimi/lab/issues/607)) ([7fecdae](https://github.com/sabertazimi/lab/commit/7fecdae1f27a4c636943b87eb2f2efa0ae192213))

### Features

- **mortal:** add Mortal GUI Vue project ([#602](https://github.com/sabertazimi/lab/issues/602)) ([62baa1e](https://github.com/sabertazimi/lab/commit/62baa1edea6eca0ab331cf9c221953824854199a))

# [1.8.0](https://github.com/sabertazimi/lab/compare/v1.7.1...v1.8.0) (2022-08-29)

**Note:** Version bump only for package @lab/vue-design

## [1.7.1](https://github.com/sabertazimi/lab/compare/v1.7.0...v1.7.1) (2022-05-27)

**Note:** Version bump only for package @lab/vue-design

# [1.7.0](https://github.com/sabertazimi/lab/compare/v1.6.1...v1.7.0) (2022-03-24)

### Bug Fixes

- **vue-design:** update vitrual DOM and apply to DOM ([#271](https://github.com/sabertazimi/lab/issues/271)) ([8c81318](https://github.com/sabertazimi/lab/commit/8c813187236e6b3594bb8663d6f38498d95c3964))

### Features

- **vue-design:** setup demo for vue design learning ([#269](https://github.com/sabertazimi/lab/issues/269)) ([4bbb62e](https://github.com/sabertazimi/lab/commit/4bbb62efa32436f4d59a8fb06b9dbd6809843c48))
