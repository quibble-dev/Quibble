import { generate_id } from '$lib/functions/generate_id';

type ToastIn = {
  message: string;
  class?: string;
  duration?: number;
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
    const exists = toasts.find((t) => t.message === toast.message);
    if (exists !== undefined) return exists.id;

    const new_toast: Toast = {
      ...toast,
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
