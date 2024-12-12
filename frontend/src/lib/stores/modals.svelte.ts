import { SvelteMap } from 'svelte/reactivity';

const modals = ['auth'] as const;
type IModals = (typeof modals)[number];

const modals_state = $state(
  new SvelteMap<IModals, boolean>(modals.map((item) => [item, false]))
);

export function createModalsStore() {
  return {
    get state() {
      return modals_state;
    },
    open(modal: IModals) {
      modals_state.keys().forEach((key) => {
        modals_state.set(key, false);
      });
      modals_state.set(modal, true);
    },
    close(modal: IModals) {
      modals_state.set(modal, false);
    }
  };
}
