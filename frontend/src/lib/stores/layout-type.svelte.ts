import { browser } from '$app/environment';

type LayoutType = 'card' | 'compact';

const DEFAULT_LAYOUT_TYPE: LayoutType = 'card';
const LAYOUT_TYPE_LOCALSTORAGE_KEY = 'layout-type';

function get_stored_layout_type(): LayoutType {
  if (!browser) return DEFAULT_LAYOUT_TYPE;

  const stored = localStorage.getItem(LAYOUT_TYPE_LOCALSTORAGE_KEY);
  return stored === 'card' || stored === 'compact' ? stored : DEFAULT_LAYOUT_TYPE;
}

function create_layout_type_store() {
  let layout_type = $state<LayoutType>(get_stored_layout_type());

  return {
    get value() {
      return layout_type;
    },
    update(type: LayoutType) {
      layout_type = type;
      if (browser) {
        localStorage.setItem(LAYOUT_TYPE_LOCALSTORAGE_KEY, type);
      }
    },
    reset() {
      this.update(DEFAULT_LAYOUT_TYPE);
    }
  };
}

// initialize store
export const layout_type_store = create_layout_type_store();
