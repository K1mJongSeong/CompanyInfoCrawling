export default function TermsPage() {
  return (
    <div
      className="w-screen relative flex items-center justify-center py-10 bg-fixed  min-h-[900px]"
      style={{
        backgroundImage: "url('/assets/images/terms_bg.png",
        backgroundPosition: "center",
      }}
    >
      <div className="w-[calc(100%-32px)] max-w-2xl bg-white rounded-lg max-h-[calc(100%-100px)] py-7 px-4 lg:py-14 lf:px-10 flex flex-col gap-7 items-center">
        <div className="text-lg font-bold">TERMS & Conditions</div>
        <div className="w-full max-h-[650px] overflow-y-auto text-sm text-gray-900">
          <iframe
            className="w-full min-h-[500px]"
            src="/assets/terms/terms_english.html"
            frameBorder={0}
          ></iframe>
        </div>
      </div>
    </div>
  );
}
