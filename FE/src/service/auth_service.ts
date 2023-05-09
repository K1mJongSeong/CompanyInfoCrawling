import client from "./api/client";

export interface InBasicRegisterProps {
  name: string;
  password: string;
  email: string;
  country: string;
}
export interface InCorUserRegisterProps extends InBasicRegisterProps {
  corporate_name: string;
  business_num: string;
}
export interface InCountry {
  name: string;
  code: string;
}

interface InVerifyCodeProps {
  email: string;
  code: string;
}

export const SendEmailVerify = async (email: string) => {
  const res = await client.post("/send_email_verification/", { email });
  const data = await res.data;
  return data;
};

export const VerifyCode = async ({ email, code }: InVerifyCodeProps) => {
  const res = await client.post("/verfication/", {
    email,
    auth_num: code,
  });
  const data = await res.data;
  return data;
};

export const UserRegister = async ({
  name,
  password,
  email,
  country,
}: InBasicRegisterProps): Promise<{ message: string }> => {
  const res = await client.post("/UserJoin/", {
    name,
    password,
    email,
    country,
  });
  const data = await res.data;
  return data;
};

export const CoUserRegister = async ({
  name,
  password,
  email,
  country,
  corporate_name,
  business_num,
}: InCorUserRegisterProps): Promise<{ message: string }> => {
  const res = await client.post("/CorJoin/", {
    name,
    password,
    email,
    country,
    corporate_name,
    business_num,
  });
  const data = await res.data;
  return data;
};

export const ChangePw = async ({
  email,
  password,
}: {
  email: string;
  password: string;
}) => {
  const res = await client.put(`/ChangePassword/${email}`, {
    email,
    password,
  });
  const data = await res.data;
  return data;
};
