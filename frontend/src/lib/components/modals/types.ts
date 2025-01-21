export type FormConfig = Record<string, Promise<typeof import('*.svelte')>>;

export type Forms<Config extends FormConfig> = keyof Config;

export type FormsState<Config extends FormConfig> = { [K in keyof Config]: object };

export type FormProps<Config extends FormConfig> = {
  forms_state: FormsState<Config>;
  update_forms_state: (form: keyof Config, data: FormSubmitData) => void;
  goto_form: (form: keyof Config) => void;
};

export type FormSubmitData = {
  [key: string]: unknown | FormSubmitData | Array<unknown>;
};
