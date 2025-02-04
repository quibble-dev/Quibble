import { generate_id } from '$lib/functions/generate-id';

type Options = {
  class?: string;
  duration?: number;
  inside_modal?: boolean;
};

type Toast = Options & {
  id: string;
  timer: NodeJS.Timeout;
  message: string;
};

let toasts = $state<Toast[]>([]);

export const toast = {
  get toasts() {
    return toasts;
  },
  push: (message: string, options?: Options) => {
    const exists = toasts.find(
      (t) => t.message === message && t.inside_modal === options?.inside_modal
    );
    if (exists !== undefined) return exists.id;

    const new_toast: Toast = {
      ...options,
      message,
      inside_modal: options?.inside_modal ?? false,
      id: generate_id(),
      timer: setTimeout(() => {
        toasts = toasts.filter((t) => t.id !== new_toast.id);
      }, options?.duration ?? 3000)
    };

    toasts.push(new_toast);
    return new_toast.id;
  },
  dismiss: (id: string) => {
    const toast = toasts.find((t) => t.id === id);
    if (toast === undefined) return;

    clearTimeout(toast.timer);
    toasts = toasts.filter((t) => t.id !== id);
  }
};
