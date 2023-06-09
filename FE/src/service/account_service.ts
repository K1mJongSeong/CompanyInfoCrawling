import client from "./api/client";

export async function getUserInfo({ email }: { email: string }) {
  const res = await client.get(`/UserGET/${email}/`);
  const data = await res.data;
  return data;
}
export async function getCorUserInfo({ email }: { email: string }) {
  const res = await client.get(`/CorUserGET/${email}/`);
  const data = await res.data;
  return data;
}

export async function changeUserInfo({
  name,
  password,
  email,
  country,
  phone,
  auth_state,
}: {
  name: string;
  password: string;
  email: string;
  country: string;
  phone: string;
  auth_state: string;
}) {
  const res = await client.put(`/UserPUT/${email}/`, {
    name,
    password,
    email,
    country,
    phone,
    auth_state,
  });
  const data = await res.data;
  return data;
}
export async function changeCorUserInfo({
  name,
  password,
  email,
  country,
  phone,
  corporate_name,
  business_num,
  auth_state,
}: {
  name: string;
  password: string;
  email: string;
  country: string;
  phone: string;
  corporate_name: string;
  business_num: string;
  auth_state: string;
}) {
  const res = await client.put(`/CorUserPUT/${email}/`, {
    name,
    password,
    email,
    country,
    phone,
    auth_state,
    corporate_name,
    business_num,
  });
  const data = await res.data;
  return data;
}

export async function deleteUser({ email }: { email: string }) {
  const res = await client.put(`/UserWithdrawalUpdate/${email}/`, {
    auth_state: "정지",
  });
  const data = await res.data;
  return data;
}
export async function deleteCorUser({ email }: { email: string }) {
  const res = await client.put(`/CorUserWithdrawalUpdate/${email}/`, {
    auth_state: "정지",
  });
  const data = await res.data;
  return data;
}
