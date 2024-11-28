import { isAuthError } from "$lib/errors/auth";
import { apiFetch } from "$lib/utils/api";
import { fail } from "@sveltejs/kit";
import type { Actions } from "./$types";

export const actions = {
  create: async ({ request }) => {
    const form_data = await request.formData()

    try {
      await apiFetch('v1/user/me/profiles/', {
        headers: {
          Authorization: `Bearer ${form_data.get('auth_token')}`
        },
        body: JSON.stringify({
          username: form_data.get('username'),
        })
      });

      return { success: true };
    } catch (err) {
      let message = 'Oops! something went wrong.';
      let code = 500;

      if (isAuthError(err)) {
        message = err.message;
        code = err.code;
      } else {
        console.error(err);
      }
      return fail(code, { detail: message });
    }
  },
} satisfies Actions;
