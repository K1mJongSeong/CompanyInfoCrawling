"use client";
import {
  Button,
  Dialog,
  DialogActions,
  DialogContent,
  DialogContentText,
  DialogTitle,
} from "@mui/material";

interface Props {
  title: string;
  message: string;
  open: boolean;
  close: () => void;
  onClick: () => void;
}

export default function AccountDialog({
  title,
  message,
  open,
  close,
  onClick,
}: Props) {
  return (
    <Dialog
      open={open}
      onClose={close}
      aria-labelledby="alert-dialog-title"
      aria-describedby="alert-dialog-description"
    >
      <DialogTitle id="alert-dialog-title">{title}</DialogTitle>
      {message && (
        <DialogContent>
          <DialogContentText id="alert-dialog-description">
            {message}
          </DialogContentText>
        </DialogContent>
      )}
      <DialogActions>
        <Button onClick={close}>Cancel</Button>
        <Button onClick={onClick} autoFocus>
          OK
        </Button>
      </DialogActions>
    </Dialog>
  );
}
