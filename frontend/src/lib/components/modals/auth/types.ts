export type FormSubmitData = Record<string, string | number | undefined>;

type Forms = {
	login: FormSubmitData;
	profile_select: FormSubmitData;
};

export type FormsState = { [K in keyof Forms]: {} };

export type FormProps = {
	forms_state: FormsState;
	on_submit: (data: FormSubmitData) => void;
	goto_form: (form: keyof Forms) => void;
};
