import type { Comment, CommentTree } from '$lib/types/comment';

export class CommentTreeBuilder {
  #tree: CommentTree[] = [];

  constructor(private json: Comment[] = []) {
    // NOTE: might do more operations in future
    this.#tree = this.convert_to_tree(this.json);
  }

  private convert_to_tree(data: Comment[]) {
    const tree: CommentTree[] = [];
    const node_map: { [path: string]: CommentTree } = {};

    // initialize node_map with empty children array
    data.forEach((node) => {
      const _node = { ...node, children: [] };
      node_map[String(node.path)] = _node;

      if (!node.path?.includes('.')) {
        // top-level comment, no parent
        tree.push(_node);
      }
    });

    // populate tree by referencing parent
    data.forEach((node) => {
      const path_parts = node.path?.split('.');
      const parent_path = path_parts?.slice(0, -1).join('.');
      const parent_node = node_map[String(parent_path)];

      if (parent_node) {
        parent_node.children.push(node);
      }
    });

    return tree;
  }

  public build() {
    return this.#tree;
  }
}
