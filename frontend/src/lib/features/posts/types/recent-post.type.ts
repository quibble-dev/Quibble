export type Post = {
  id: string;
  community: {
    avatar?: string | null | undefined;
    name: string;
  };
  title: string;
  slug?: string | undefined;
  cover?: string | null | undefined;
  upvotes?: number[] | undefined;
  comments?: number[] | undefined;
};

export type RecentPost = Post & {
  timestamp: Date;
};
