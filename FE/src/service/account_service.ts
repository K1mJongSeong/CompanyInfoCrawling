import client from "./api/client";

export async function getUserInfo({ email }: { email: string }) {
  const res = await client.get(`/UserGET/${email}/`);
  const data = await res.data;
  return data;
}
