export type FormSubmitData = Record<string, string | number | undefined>;

type Forms = {
	login: FormSubmitData;
};

export type FormsState = { [K in keyof Forms]: {} };

export type FormProps = {
	forms_state: FormsState;
	on_submit: (data: FormSubmitData) => void;
};
