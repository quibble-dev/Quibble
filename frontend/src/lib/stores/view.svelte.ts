import { browser } from '$app/environment';

type ViewState = 'card' | 'compact';

const default_view: ViewState = 'card';

const stored_view_state: ViewState = browser
  ? ((localStorage.getItem('view') as ViewState) ?? default_view)
  : default_view;

let view_state = $state<ViewState>(stored_view_state);

$effect.root(() => {
  $effect(() => {
    // auto sync to localStorage on state update
    localStorage.setItem('view', view_state);
  });
});

export function createViewStore() {
  return {
    get state() {
      return view_state;
    },
    update(view: ViewState) {
      view_state = view;
    }
  };
}
