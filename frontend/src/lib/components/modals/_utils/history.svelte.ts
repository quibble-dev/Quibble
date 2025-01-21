import type { FormConfig } from '../types';

export function create_form_history<T extends FormConfig>(initial_form: keyof T) {
  let history = $state([initial_form]);

  function go_to_form(form: keyof T) {
    // if navigating to a form thats already in the history stack,
    // truncate the stack upto the most recent occurance of that form
    // (avoiding duplicate entiries)
    const form_index = history.findIndex((entry) => entry === form);
    if (form_index > -1) {
      // if exists
      history = history.slice(0, form_index + 1);
    } else {
      // otherwise, push current form to prev_form_history
      history.push(form);
    }
    return history.at(-1);
  }

  function go_back() {
    if (history.length > 1) {
      // remove current form from history stack
      history.pop();
    }
    return history.at(-1);
  }

  return {
    get history() {
      return history;
    },
    go_to_form,
    go_back
  };
}
