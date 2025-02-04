import { generate_id } from '$lib/functions/generate-id';

type ToastIn = {
  message: string;
  class?: string;
  duration?: number;
  inside_modal?: boolean;
};

type Toast = ToastIn & {
  id: string;
  timer: NodeJS.Timeout;
};

let toasts = $state<Toast[]>([]);

export const toast = {
  get toasts() {
    return toasts;
  },
  push: (toast: ToastIn) => {
    const exists = toasts.find(
      (t) => t.message === toast.message && t.inside_modal === t.inside_modal
    );
    if (exists !== undefined) return exists.id;

    const new_toast: Toast = {
      ...toast,
      inside_modal: toast.inside_modal ?? false,
      id: generate_id(),
      timer: setTimeout(() => {
        toasts = toasts.filter((t) => t.id !== new_toast.id);
      }, toast.duration ?? 3000)
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
