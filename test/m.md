### Key GitHub-Flavored Markdown Features Supported by Streamlit:

- **Headings**: Using `#` for different levels of headings.
- **Lists**: Unordered (`-` or `*`) and ordered (`1.`).
- **Task Lists**: Use `- [x]` for completed tasks and `- [ ]` for pending tasks.
- **Code Blocks**: Fenced code blocks using triple backticks (\`\`\`), with support for syntax highlighting.
- **Tables**: Tables with `|` separator and `-` for row separation.
- **Links**: Markdown links using `[text](URL)`.

### Explanation of GitHub-Flavored Markdown:

1. **Headings**: You can create different levels of headings by increasing the number of `#` symbols. For example, `# Heading 1` will render a level 1 heading, and `## Heading 2` will render a level 2 heading.
2. **Lists**: Use `-` or `*` for unordered lists and `1.` for ordered lists.
3. **Task Lists**: GitHub-flavored Markdown supports checkboxes like `- [x]` for completed tasks and `- [ ]` for tasks that are still pending.
4. **Code Blocks**: You can display code with syntax highlighting by enclosing your code in triple backticks. You can also specify the programming language after the backticks, e.g., ` ```python ` for Python code blocks.
5. **Tables**: Markdown supports simple tables using `|` to separate columns and `-` to create a row.

### Advanced: Rendering GitHub Markdown from a File

If you want to load and display a markdown file from GitHub or any local file that uses GitHub-flavored markdown, you can do the following:

1. **Load Markdown from a file**:
   - If the markdown file is hosted on GitHub, you can fetch it using `requests`.
   - If it's a local file, simply read it.

### Example: Loading and Rendering Markdown from a File
