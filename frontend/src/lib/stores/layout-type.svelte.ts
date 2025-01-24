import { browser } from '$app/environment';

type LayoutType = 'card' | 'compact';

const default_layout_type: LayoutType = 'card';

const stored_layout_type: LayoutType = browser
  ? ((localStorage.getItem('layout_type') as LayoutType) ?? default_layout_type)
  : default_layout_type;

let layout_type = $state<LayoutType>(stored_layout_type);

export function createLayoutTypeStore() {
  return {
    get state() {
      return layout_type;
    },
    update(type: LayoutType) {
      layout_type = type;
      // auto sync to localStorage on state update
      localStorage.setItem('layout_type', type);
    }
  };
}
