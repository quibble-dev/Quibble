import forms from './forms';

export type FormSubmitData = {
  [key: string]: string | number | undefined | FormSubmitData | Array<unknown>;
};

export type Forms = keyof typeof forms;

export type FormsState = { [K in Forms]: object };

export type FormProps = {
  forms_state: FormsState;
  update_forms_state: (form: Forms, data: FormSubmitData) => void;
  goto_form: (form: Forms) => void;
};
