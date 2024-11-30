export function stopEventPropagation(e: Event) {
  e.stopPropagation();
  e.preventDefault();
}