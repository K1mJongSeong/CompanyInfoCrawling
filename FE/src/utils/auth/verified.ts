import { SendEmailVerify } from "@/service/auth_service";
import { EnqueueSnackbar } from "notistack";

export default class VerifyAuth {
  async verifyEmail(email: string, enqueueSnackbar: EnqueueSnackbar) {
    try {
      if (!email) {
        enqueueSnackbar("Enter Email!", { variant: "warning" });
        return false;
      }
      const emailRule =
        /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
      const testResult = await emailRule.test(email);
      if (!testResult) {
        enqueueSnackbar("Not Email!", { variant: "warning" });
        return false;
      }
      const result = await SendEmailVerify(email);
      if (result.message === "인증번호가 이메일로 발송되었습니다.") {
        enqueueSnackbar("Send Email!", { variant: "success" });
        return true;
      }
    } catch (err) {
      enqueueSnackbar("Server Error", { variant: "error" });
      return false;
    }
  }
}
