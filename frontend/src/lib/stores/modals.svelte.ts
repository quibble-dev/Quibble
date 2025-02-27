import { SvelteMap } from 'svelte/reactivity';

const modals_map = ['auth'] as const;
type Modals = (typeof modals_map)[number];

const modals = $state(new SvelteMap<Modals, boolean>(modals_map.map((item) => [item, false])));

export function createModalsStore() {
  return {
    get state() {
      return modals;
    },
    open(modal: Modals) {
      modals.keys().forEach((key) => modals.set(key, false));
      modals.set(modal, true);
    },
    close(modal: Modals) {
      modals.set(modal, false);
    }
  };
}
