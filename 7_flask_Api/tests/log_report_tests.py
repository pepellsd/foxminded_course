import unittest
import datetime
from get_drivers import driver_result, Log, Web_report


class TestLog(unittest.TestCase):
    def test_get_logs_true(self):
        log = Log(path="/data")
        self.assertEqual(log.get_logs()[0], list_abbr)
        self.assertEqual(log.get_logs()[1], list_start)
        self.assertEqual(log.get_logs()[2], list_end)

    def test_get_logs_false(self):
        log = Log(path="/some_path")
        with self.assertRaises(FileNotFoundError):
            self.assertEqual(log.get_logs(), "directory not found or  incorrect names of files")

    def test_validate_logs(self):
        log = Log(path="/data")
        log.get_logs()
        log.abbr_list.append("some_extra")
        with self.assertRaises(SystemExit):
            self.assertEqual(log.validate(), "data is not full")
        log.abbr_list.pop()
        log.end_list[5] = "incorrect string data"
        with self.assertRaises(SystemExit) as e:
            self.assertEqual(log.validate(), e.exception.args[0])


class TestWebReport(unittest.TestCase):
    small_list_abbr = ['CSR_Carlos Sainz_RENAULT', 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER']
    small_list_start = ['CSR2018-05-24_12:03:15.145', 'DRR2018-05-24_12:14:12.054']
    small_list_end = ['CSR2018-05-24_1:04:28.095', 'DRR2018-05-24_1:11:24.067']
    result_drivers = [['Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '0:57:12.013', 'DRR', 1],
                      ['Carlos Sainz', 'RENAULT', '1:01:12.950', 'CSR', 2]]

    def test_get_diff_info(self):
        report = Web_report(abbr_list=self.small_list_abbr,
                            start_list=self.small_list_start,
                            end_list=self.small_list_end)
        report.get_diff()
        self.assertEqual(report.diff_list, [datetime.timedelta(seconds=3672, microseconds=950000),
                                            datetime.timedelta(seconds=3432, microseconds=13000)])
        result = report.get_info()
        self.assertEqual(result, self.result_drivers)

    def test_drivers_asc_all(self):
        # нет теста для фукции read_logs_driver_info так как там просто собраны методы двух классов
        result = driver_result(data=self.result_drivers)
        self.assertEqual(result, self.result_drivers)

    def test_drivers_desc_all(self):
        result = driver_result(data=self.result_drivers, order_asc=False)
        self.assertEqual(self.result_drivers[::-1], result)

    def test_solo_driver(self):
        result = driver_result(data=self.result_drivers,
                               filter="DRR")
        self.assertEqual(['Daniel Ricciardo', 'RED BULL RACING TAG HEUER', '0:57:12.013', 'DRR', 1], result)


# list for test class Log
list_abbr = ['BHS_Brendon Hartley_SCUDERIA TORO ROSSO HONDA', 'CLS_Charles Leclerc_SAUBER FERRARI',
             'CSR_Carlos Sainz_RENAULT', 'DRR_Daniel Ricciardo_RED BULL RACING TAG HEUER',
             'EOF_Esteban Ocon_FORCE INDIA MERCEDES', 'FAM_Fernando Alonso_MCLAREN RENAULT',
             'KMH_Kevin Magnussen_HAAS FERRARI', 'KRF_Kimi RГ¤ikkГ¶nen_FERRARI', 'LHM_Lewis Hamilton_MERCEDES',
             'LSW_Lance Stroll_WILLIAMS MERCEDES', 'MES_Marcus Ericsson_SAUBER FERRARI', 'NHR_Nico Hulkenberg_RENAULT',
             'PGS_Pierre Gasly_SCUDERIA TORO ROSSO HONDA', 'RGH_Romain Grosjean_HAAS FERRARI',
             'SPF_Sergio Perez_FORCE INDIA MERCEDES', 'SSW_Sergey Sirotkin_WILLIAMS MERCEDES',
             'SVF_Sebastian Vettel_FERRARI', 'SVM_Stoffel Vandoorne_MCLAREN RENAULT', 'VBM_Valtteri Bottas_MERCEDES']

list_end = ['BHS2018-05-24_1:16:05.164', 'CLS2018-05-24_1:10:54.750', 'CSR2018-05-24_1:04:28.095',
            'DRR2018-05-24_1:11:24.067', 'EOF2018-05-24_1:12:11.838', 'FAM2018-05-24_1:14:17.169',
            'KMH2018-05-24_1:04:04.396', 'KRF2018-05-24_1:04:13.889', 'LHM2018-05-24_1:11:32.585',
            'LSW2018-05-24_1:07:26.834', 'MES2018-05-24_1:05:58.778', 'NHR2018-05-24_1:04:02.979',
            'PGS2018-05-24_1:08:36.586', 'RGH2018-05-24_1:06:27.441', 'SPF2018-05-24_1:13:13.883',
            'SSW2018-05-24_1:11:24.354', 'SVF2018-05-24_1:04:03.332', 'SVM2018-05-24_1:19:50.198',
            'VBM2018-05-24_1:01:12.434']

list_start = ['BHS2018-05-24_12:14:51.985', 'CLS2018-05-24_12:09:41.921', 'CSR2018-05-24_12:03:15.145',
              'DRR2018-05-24_12:14:12.054', 'EOF2018-05-24_12:17:58.810', 'FAM2018-05-24_12:13:04.512',
              'KMH2018-05-24_12:02:51.003', 'KRF2018-05-24_12:03:01.250', 'LHM2018-05-24_12:18:20.125',
              'LSW2018-05-24_12:06:13.511', 'MES2018-05-24_12:04:45.513', 'NHR2018-05-24_12:02:49.914',
              'PGS2018-05-24_12:07:23.645', 'RGH2018-05-24_12:05:14.511', 'SPF2018-05-24_12:12:01.035',
              'SSW2018-05-24_12:16:11.648', 'SVF2018-05-24_12:02:58.917', 'SVM2018-05-24_12:18:37.735',
              'VBM2018-05-24_12:00:00.000']


if __name__ == "__main__":
    unittest.main()