import { browser } from '$app/environment';

type LayoutState = 'card' | 'compact';

const default_layout: LayoutState = 'card';

const stored_layout_state: LayoutState = browser
  ? ((localStorage.getItem('layout') as LayoutState) ?? default_layout)
  : default_layout;

let layout_state = $state<LayoutState>(stored_layout_state);

$effect.root(() => {
  $effect(() => {
    // auto sync to localStorage on state update
    localStorage.setItem('layout', layout_state);
  });
});

export function createLayoutStore() {
  return {
    get state() {
      return layout_state;
    },
    update(layout: LayoutState) {
      layout_state = layout;
    }
  };
}
