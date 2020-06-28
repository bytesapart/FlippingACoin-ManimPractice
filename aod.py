from pygments.style import Style
from pygments.token import Keyword, Name, Comment, String, Error, \
    Literal, Number, Operator, Other, Punctuation, Text, Generic, \
    Whitespace


class AodStyle(Style):
    background_color = "#282c34"
    default_style = ""

    styles = {
        Comment: "#59626f",
        Comment.Hashbang: "#59626f",
        Comment.Multiline: "#59626f",
        Comment.Preproc: "#ff79c6",
        Comment.Single: "#6272a4",
        Comment.Special: "#6272a4",

        Generic: "#C3D3DE",
        Generic.Deleted: "#8b080b",
        Generic.Emph: "#C3D3DE underline",
        Generic.Error: "#C3D3DE",
        Generic.Heading: "#C3D3DE bold",
        Generic.Inserted: "#C3D3DE bold",
        Generic.Output: "#44475a",
        Generic.Prompt: "#C3D3DE",
        Generic.Strong: "#C3D3DE",
        Generic.Subheading: "#C3D3DE bold",
        Generic.Traceback: "#C3D3DE",

        Error: "#C3D3DE",

        Keyword: "#c679DD italic",
        Keyword.Constant: "#c679DD italic",
        Keyword.Declaration: "#c679DD italic",
        Keyword.Namespace: "#c679DD",
        Keyword.Pseudo: "#c679DD",
        Keyword.Reserved: "#c679DD",
        Keyword.Type: "#c679DD",

        Literal: "#C3D3DE",
        Literal.Date: "#C3D3DE",

        Name: "#C3D3DE",
        Name.Attribute: "#50fa7b",
        Name.Builtin: "#61aeef italic",
        Name.Builtin.Pseudo: "#C3D3DE",
        Name.Class: "#50fa7b",
        Name.Constant: "#C3D3DE",
        Name.Decorator: "#C3D3DE",
        Name.Entity: "#C3D3DE",
        Name.Exception: "#C3D3DE",
        Name.Function: "#50fa7b",
        Name.Label: "#61aeef italic",
        Name.Namespace: "#C3D3DE",
        Name.Other: "#C3D3DE",
        Name.Tag: "#ff79c6",
        Name.Variable: "#61aeef italic",
        Name.Variable.Class: "#61aeef italic",
        Name.Variable.Global: "#61aeef italic",
        Name.Variable.Instance: "#61aeef italic",

        Number: "#d19a66",
        Number.Bin: "#d19a66",
        Number.Float: "#d19a66",
        Number.Hex: "#d19a66",
        Number.Integer: "#d19a66",
        Number.Integer.Long: "#d19a66",
        Number.Oct: "#d19a66",

        Operator: "#61aeef",
        Operator.Word: "#c679DD",

        Other: "#C3D3DE",

        Punctuation: "#C3D3DE",

        String: "#98C379",
        String.Backtick: "#98C379",
        String.Char: "#98C379",
        String.Doc: "#98C379",
        String.Double: "#98C379",
        String.Escape: "#98C379",
        String.Heredoc: "#98C379",
        String.Interpol: "#98C379",
        String.Other: "#98C379",
        String.Regex: "#98C379",
        String.Single: "#98C379",
        String.Symbol: "#98C379",

        Text: "#C3D3DE",

        Whitespace: "#C3D3DE"
    }
