import Foundation
import RealmSwift

class dashBoardData: Object {
    @objc dynamic var time_stamp: String? = nil
    let Pulsometer_readout = RealmOptional<Int>()
    let Engine_efficiency = RealmOptional<Double>()
    let red_Value = RealmOptional<Int>()
    let blue_Value = RealmOptional<Int>()
    let green_Value = RealmOptional<Int>()
}

