import { EnqueueSnackbar } from "notistack";

export default class VerifyAuth {
  async verifyEmail(email: string, enqueueSnackbar: EnqueueSnackbar) {
    if (!email) {
      enqueueSnackbar("Enter Email!", { variant: "warning" });
      return false;
    }
    const emailRule =
      /^[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*@[0-9a-zA-Z]([-_.]?[0-9a-zA-Z])*.[a-zA-Z]{2,3}$/i;
    const testResult = await emailRule.test(email);
    if(!testResult){
         enqueueSnackbar("Not Email!", { variant: "warning" });
         return false
    }else{
        enqueueSnackbar("Send Email!", { variant: "success" });
        return true
    }
  }
}
