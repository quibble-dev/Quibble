import { generate_id } from '$lib/functions/generate_id';

type Toast = {
  message: string;
  class?: string;
  duration?: number;
};

type ToastWithId = Toast & {
  id: string;
  timer: NodeJS.Timeout;
};

let toasts = $state<ToastWithId[]>([]);

export const toast = {
  get state() {
    return toasts;
  },
  push: (toast: Toast) => {
    const exists = toasts.find((t) => t.message === toast.message);
    if (exists !== undefined) return exists.id;

    const new_toast: ToastWithId = {
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
