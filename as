{
  "editor.fontFamily": "'Fira Code', Consolas, 'Consolas', monospace",
  "editor.fontSize": 18, // 20 thoda bada hota hai, 18 comfortable hoga
  "editor.fontLigatures": true,
  "editor.fontWeight": "400", // 300 se thoda bold ho jata hai, better readability
  "editor.lineHeight": 26, // thoda zyada line height for breathing space
  "editor.letterSpacing": 0.2, // aap already use kar rahe ho, nice hai
  "editor.renderLineHighlight": "gutter", // line highlight gutter me dikhana

  "editor.minimap.enabled": false,
  "editor.guides.bracketPairs": "active",

  "editor.cursorStyle": "line",
  "editor.cursorBlinking": "smooth", // smooth blinking cursor look ke liye
  "editor.cursorSmoothCaretAnimation": "on",
  "editor.smoothScrolling": true,

  "editor.wordWrap": "bounded",
  "editor.wordWrapColumn": 120, // 150 se kam rakho, readability ke liye best hota hai

  "files.autoSave": "afterDelay",
  "files.autoSaveDelay": 1000, // 1 second baad auto save ho

  "files.associations": {
    ".env*": "dotenv"
  },

  // Formatter settings (sab files me prettier lage)
  "[javascript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescript]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[typescriptreact]": {
    "editor.defaultFormatter": "vscode.typescript-language-features"
  },
  "[json]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[css]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[scss]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[html]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },
  "[jsonc]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  "prettier.printWidth": 120,
  "prettier.trailingComma": "all",

  // Git settings
  "git.enableSmartCommit": true,
  "git.autofetch": true,
  "git.confirmSync": false,

  // Terminal
  "terminal.integrated.fontFamily": "'Fira Code', monospace",
  "terminal.integrated.fontSize": 14,

  // Disable power mode for now
  "powermode.enabled": true,
  "powermode.combo.counterEnabled": "hide",
  "powermode.intensity": 0.3,
  "powermode.combo.counterSize": 0,
  "powermode.shake.enabled": false,
  "powermode.presets": "flames",
  "editor.guides.indentation": true,
  "editor.tokenColorCustomizations": {
    "[*Light*]": {
      "textMateRules": [
        {
          "scope": "ref.matchtext",
          "settings": {
            "foreground": "#000"
          }
        }
      ]
    },
    "[*Dark*]": {
      "textMateRules": [
        {
          "scope": "ref.matchtext",
          "settings": {
            "foreground": "#fff"
          }
        }
      ]
    },
    "textMateRules": []
  },
  "dotenv.enableAutocloaking": false,
  "github.copilot.nextEditSuggestions.enabled": true,
  "terminal.integrated.env.windows": {},
  "mdb.mcp.server": "prompt",
  "workbench.editorAssociations": {
    "*.copilotmd": "vscode.markdown.preview.editor",
    "*.dll": "default"
  },
  "editor.unicodeHighlight.invisibleCharacters": false,
  "claudeCode.disableLoginPrompt": true,
  "claudeCode.preferredLocation": "panel",
  "workbench.iconTheme": "material-icon-theme",
  "workbench.colorTheme": "One Dark Pro Darker",
  "update.showReleaseNotes": false,
  "workbench.startupEditor": "none",
  "github.copilot.enable": {
    "*": false,
    "plaintext": false,
    "markdown": false,
    "scminput": false
  },
  "terminal.integrated.initialHint": false
}