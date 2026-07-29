const js = require("@eslint/js");

module.exports = [
  {
    ignores: [".venv/**", "node_modules/**"],
  },
  {
    files: ["app/static/js/**/*.js"],
    ...js.configs.recommended,
    languageOptions: {
      ecmaVersion: "latest",
      sourceType: "module",
      globals: {
        window: "readonly",
        document: "readonly",
        console: "readonly",
      },
    },
  },
];
