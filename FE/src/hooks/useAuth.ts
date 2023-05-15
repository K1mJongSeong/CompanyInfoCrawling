/* eslint-disable react-hooks/exhaustive-deps */
import { Login, LoginCheck, Logout } from "@/service/auth_service";
import { useSnackbar } from "notistack";
import { useEffect, useState } from "react";

export default function useFirebaseAuth() {
  const { enqueueSnackbar } = useSnackbar();

  const [user, setUser] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  const signIn = async ({ email, pw }: { email: string; pw: string }) => {
    try {
      if (!email || !pw) {
        return enqueueSnackbar("Enter All Login Field", { variant: "warning" });
      }
      const emailRule =
        /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;

      if (!emailRule.test(email)) {
        return enqueueSnackbar("Not Email!", { variant: "warning" });
      }
      const result = await Login({ email, password: pw });
      if (result.message === "로그인에 성공했습니다.") {
        enqueueSnackbar("SUCCESS LOGIN", { variant: "success" });
        localStorage.setItem("userEmail", email);
        setUser(email);
      }
    } catch (err: any) {
      if (err.response.data.message === "존재하지 않는 아이디입니다.") {
        return enqueueSnackbar("Not User", { variant: "error" });
      } else {
        console.error(err);
        return enqueueSnackbar("Server Error", { variant: "error" });
      }
    }
  };

  const clear = () => {
    setUser(null);
    setLoading(false);
    localStorage.clear();
  };

  const signOut = async () => {
    try {
      if (!user) return clear();
      const result = await Logout({ email: user });
      if (result) {
        clear();
      }
    } catch (err) {
      console.error(err);
    }
  };

  const check = async () => {
    try {
      const userEmail = localStorage.getItem("userEmail");
      if (!userEmail) {
        clear();
        return;
      } else {
        const result = await LoginCheck({ email: userEmail });
        if (result) {
          setUser(userEmail);
          setLoading(false);
        } else {
          clear();
        }
      }
    } catch (err) {
      console.error(err);
    }
  };

  useEffect(() => {
    const userEmail = localStorage.getItem("userEmail");
    if (userEmail) {
      check();
    } else {
      clear();
    }
  }, []);

  return {
    user,
    loading,
    signIn,
    signOut,
  };
}
