import { dev } from "$app/environment";
import { fail } from "@sveltejs/kit";
import type { Actions } from "./$types";

export const actions = {
  login: async ({ cookies, request }) => {
    const form_data = await request.formData()

    const response = await fetch('http://127.0.0.1:8000/api/v1/user/auth/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json'
      },
      body: JSON.stringify({
        email: form_data.get('email'),
        password: form_data.get('password')
      })
    })

    const data = await response.json()

    if (!response.ok) {
      return fail(401, { detail: data.errors[0].detail})
    }

    cookies.set('auth_token', data.token, {
      httpOnly: true,
      secure: !dev,
      path: '/',
      sameSite: 'lax',
    })

    return { success: true }
  }
} satisfies Actions
