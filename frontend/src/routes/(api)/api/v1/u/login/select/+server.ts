import { dev } from '$app/environment';
import { json, type RequestHandler } from '@sveltejs/kit';

export const POST: RequestHandler = async ({ request, cookies }) => {
  try {
    const { id } = await request.json();

    cookies.set('auth_user_profile_id', id, {
      httpOnly: true,
      secure: !dev,
      path: '/',
      sameSite: 'lax',
      maxAge: 60 * 60 * 24 * 30 // 30 days
    });

    return json({ success: true });
  } catch (err) {
    console.error(err);
    return json({ success: false }, { status: 500 });
  }
};
