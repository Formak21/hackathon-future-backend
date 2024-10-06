from factory import db
from flask import Blueprint, jsonify, request, make_response
from model import User, Session, Feed, Bid

bp = Blueprint('bid', __name__)


@bp.route('/all', methods=['GET'])
def get_all_bid_for_projects():
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user authorized", 401)

    bids = db.session.execute(db.select(Feed).filter_by(status="IN PROGRESS")).scalars()
    sorted_bids = bids.sort(key=lambda x: x.id)
    resp_bids = []
    for b in sorted_bids:
        user = db.session.execute(db.select(User).filter_by(id=b.user_id)).scalar_one()
        ext_bid = {
            "user_id": b.user_id,
            "status": b.status,
            "user_name": user.first_name + ' ' + user.last_name
        }
        resp_bids.append(ext_bid)
    return __jsonResponse({"feeds": resp_bids}, 201)


@bp.route('/<int:bid_id>', methods=['GET'])
def get_bid_by_id(bid_id):
    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)
    if not authorized:
        return __jsonResponse("user authorized", 401)

    try:
        bid = db.session.execute(db.select(Bid)).scalar_one()
    except:
        return __jsonResponse("incorrect id", 400)

    user = db.session.execute(db.select(User).filter_by(id=bid.user_id)).scalar_one()

    resp_bid = {
        "user_id": bid.user_id,
        "status": bid.status,
        "user_name": user.first_name + ' ' + user.last_name
    }

    return __jsonResponse(resp_bid, 400)


@bp.route('/', methods=['PUT'])
def update_bid(user_id):
    data = request.get_json()

    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)

    if not authorized:
        return __jsonResponse("user unauthorized", 401)

    bid = db.session.execute(db.select(Bid)).scalar_one()

    bid.status = data.get("status") or bid.title
    db.commit()
    return __jsonResponse("bid updated", 201)


@bp.route('/', methods=['POST'])
def create_bid():
    data = request.get_json()

    req_session_id = request.cookies.get('session_id')
    authorized, user_id = __check_user_authtorized(req_session_id)

    if not authorized:
        return __jsonResponse("user unauthorized", 401)

    required = ["project_id", "role"]  # VOLONTEER / ACTIVIST
    for r in required:
        if not data.get(r):
            return __jsonResponse(f"field {data.get(r)} required", 400)

    bid = Bid()
    bid.user_id = user_id
    bid.status = "IN PROGRESS"  # IN PROGRESS / CONFIRMED / CANCELLED
    bid.project_id = data.get("project_id")
    bid.role = data.get("role")

    db.session.add(bid)
    db.session.commit()

    return __jsonResponse("bid created", 201)


def __check_user_authtorized(req_session_id):
    try:
        session = db.session.execute(db.select(Session).filter_by(session_id=req_session_id)).scalar_one()
    except:
        return False, None

    return True, session.user_id


def __jsonResponse(resp: dict or str, code: int):
    if isinstance(resp, str):
        resp = {"info": resp}

    return make_response(jsonify(resp), code)
