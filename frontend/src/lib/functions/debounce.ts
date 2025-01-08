export function debounce(fn: (...args: unknown[]) => void, t: number) {
  let timer: NodeJS.Timeout;
  return (...args: unknown[]) => {
    clearTimeout(timer);
    timer = setTimeout(() => fn(...args), t);
  };
}
