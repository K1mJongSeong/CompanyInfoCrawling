/* eslint-disable react-hooks/exhaustive-deps */
import { Login, LoginCheck, Logout } from "@/service/auth_service";
import { useSnackbar } from "notistack";
import { useEffect, useState } from "react";

export default function useFirebaseAuth() {
  const { enqueueSnackbar } = useSnackbar();

  const [user, setUser] = useState<{
    email: string;
    data: { user_name: string | null; coruser_name: string | null };
  } | null>(null);
  const [loading, setLoading] = useState(true);

  const clear = () => {
    setUser(null);
    setLoading(false);
    localStorage.clear();
  };

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
      setLoading(true);
      const result = await Login({ email, password: pw });
      if (result.message === "로그인에 성공했습니다.") {
        localStorage.setItem("userEmail", email);
        const result = await check();
        if (!result) return;
        enqueueSnackbar("SUCCESS LOGIN", { variant: "success" });
      }
    } catch (err: any) {
      clear();
      if (err.response.data.message === "존재하지 않는 아이디입니다.") {
        enqueueSnackbar("Not User", { variant: "error" });
        return;
      }
      if (err.response.data.message === "비밀번호가 틀렸습니다.") {
        enqueueSnackbar("Check Login Field", { variant: "error" });
        return;
      } else {
        console.error(err);
        return enqueueSnackbar("Server Error", { variant: "error" });
      }
    }
  };

  const signOut = async () => {
    try {
      setLoading(true);
      if (!user) return clear();
      const result = await Logout({ email: user.email });
      if (result) {
        clear();
        if (result.message === "로그아웃에 성공하였습니다.") {
          enqueueSnackbar("SUCCESS LOGOUT", { variant: "success" });
        }
      }
    } catch (err) {
      console.error(err);
      enqueueSnackbar("Server Error", { variant: "error" });
      clear();
    }
  };

  const check = async () => {
    try {
      const userEmail = localStorage.getItem("userEmail");
      if (!userEmail) {
        clear();
        return false;
      } else {
        const result = await LoginCheck({ email: userEmail });
        if (result.data.auth_state === "정상") {
          setUser({
            email: userEmail,
            data: {
              user_name: result.data.user_name ? result.data.user_name : null,
              coruser_name: result.data.coruser_name
                ? result.data.coruser_name
                : null,
            },
          });
          setLoading(false);
          return true;
        } else if (result.data.auth_state === "정지") {
          enqueueSnackbar("Deactivated account", { variant: "error" });
          clear();
          return false;
        } else {
          clear();
          return false;
        }
      }
    } catch (err) {
      console.error(err);
      clear();
      return false;
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
