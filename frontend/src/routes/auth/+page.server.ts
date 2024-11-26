import { dev } from "$app/environment";
import type { Actions } from "./$types";

export const actions = {
  login: async ({ cookies, request }) => {
    const form_data = await request.formData()

    cookies.set('auth_token', form_data.get('email') as string, {
      httpOnly: true,
      secure: !dev,
      path: '/',
      sameSite: 'lax',
    })

    return { success: true }
  }
} satisfies Actions
