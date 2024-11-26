import type { Actions } from "./$types";

export const actions = {
  login: async ({ cookies, request }) => {
    const form_data = await request.formData()

    cookies.set('email', form_data.get('email') as string, {
      httpOnly: true,
      path: '/'
    })

    console.log('Cookie set!')

    return { success: true }
  }
} satisfies Actions
