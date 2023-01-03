{
  "targets": [
    {
      "target_name": "tree_sitter_http_binding",
      "include_dirs": [
        "<!(node -e \"require('nan')\")",
        "src"
      ],
      "sources": [
		# breaks tree-sitter-cli generate
        # "bindings/node/binding.cc",
        "src/parser.c",
        # If your language uses an external scanner, add it here.
      ],
      "cflags_c": [
        "-std=c99",
      ]
    }
  ]
}
