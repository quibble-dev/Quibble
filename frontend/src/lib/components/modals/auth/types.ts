import forms from './forms';

export type FormSubmitData = Record<string, string | number | undefined>;

export type Forms = keyof typeof forms;

export type FormsState = { [K in Forms]: {} };

export type FormProps = {
	forms_state: FormsState;
	on_submit: (data: FormSubmitData) => void;
	goto_form: (form: Forms) => void;
};
