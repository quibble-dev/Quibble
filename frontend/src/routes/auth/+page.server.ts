import type { Actions } from "./$types";

export const actions = {
  login: async (event) => {
    console.log('[SERVER]: got login request')

    return { success: true }
  }
} satisfies Actions
